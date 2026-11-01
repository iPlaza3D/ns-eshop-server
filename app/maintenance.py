"""Safe library maintenance helpers.

The maintenance API is deliberately preview-first: duplicate detection never deletes
anything by itself, and every destructive operation verifies the file's digest again
before removing it.
"""
import datetime
import hashlib
import json
import logging
import os
import shutil
from pathlib import Path

from constants import ALLOWED_EXTENSIONS, CONFIG_DIR, DATA_DIR, DB_FILE, CONFIG_FILE

logger = logging.getLogger('main')
CHANGE_LOG = os.path.join(DATA_DIR, 'maintenance-log.jsonl')
BACKUP_DIR = os.path.join(DATA_DIR, 'backups')


def _roots(library_paths):
    return [os.path.realpath(os.path.abspath(path)) for path in library_paths
            if os.path.isdir(path)]


def _inside(path, roots):
    candidate = os.path.realpath(os.path.abspath(path))
    return any(os.path.commonpath((candidate, root)) == root for root in roots)


def iter_game_files(library_paths):
    for root in _roots(library_paths):
        for dirpath, _dirnames, filenames in os.walk(root):
            for filename in filenames:
                if Path(filename).suffix.lower().lstrip('.') in ALLOWED_EXTENSIONS:
                    yield os.path.join(dirpath, filename)


def sha256_file(path, chunk_size=1024 * 1024):
    digest = hashlib.sha256()
    with open(path, 'rb') as source:
        while chunk := source.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def find_duplicate_groups(library_paths):
    by_size = {}
    for path in iter_game_files(library_paths):
        try:
            by_size.setdefault(os.path.getsize(path), []).append(path)
        except OSError:
            continue

    groups = []
    for size, paths in by_size.items():
        if len(paths) < 2:
            continue
        by_hash = {}
        for path in paths:
            try:
                by_hash.setdefault(sha256_file(path), []).append(path)
            except OSError:
                continue
        for digest, matches in by_hash.items():
            if len(matches) > 1:
                matches.sort(key=lambda item: (os.path.getmtime(item), item))
                groups.append({
                    'sha256': digest,
                    'size': size,
                    'keep': matches[0],
                    'duplicates': matches[1:],
                    'files': matches,
                })
    return groups


def _record(event, **payload):
    os.makedirs(DATA_DIR, exist_ok=True)
    entry = {
        'timestamp': datetime.datetime.utcnow().replace(microsecond=0).isoformat() + 'Z',
        'event': event,
        **payload,
    }
    with open(CHANGE_LOG, 'a', encoding='utf-8') as log:
        log.write(json.dumps(entry, ensure_ascii=False) + '\n')
    return entry


def record_move(source, destination):
    return _record('move', source=source, destination=destination)


def record_delete(path, sha256, reason='duplicate'):
    return _record('delete', path=path, sha256=sha256, reason=reason)


def undo_move(change, library_paths):
    """Undo one logged move, only while both paths still match the log state."""
    if change.get('event') != 'move':
        raise ValueError('Only move entries can be undone.')
    source = change.get('source')
    destination = change.get('destination')
    roots = _roots(library_paths)
    if not source or not destination or not _inside(source, roots) or not _inside(destination, roots):
        raise ValueError('The logged paths are outside the configured libraries.')
    if not os.path.isfile(destination) or os.path.exists(source):
        raise ValueError('The move cannot be undone because the filesystem changed.')
    os.makedirs(os.path.dirname(source), exist_ok=True)
    shutil.move(destination, source)
    from db import update_file_path
    library_root = next(root for root in roots if _inside(source, [root]))
    update_file_path(library_root, destination, source)
    return _record('undo_move', source=destination, destination=source, undo_of=change)


def list_changes(limit=100):
    if not os.path.isfile(CHANGE_LOG):
        return []
    with open(CHANGE_LOG, encoding='utf-8') as log:
        entries = [json.loads(line) for line in log if line.strip()]
    return entries[-max(1, min(int(limit), 500)):][::-1]


def backup_state():
    """Create a recoverable config/database snapshot before bulk maintenance."""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    stamp = datetime.datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    target = os.path.join(BACKUP_DIR, stamp)
    os.makedirs(target, exist_ok=True)
    copied = []
    for source in (CONFIG_FILE, DB_FILE):
        if os.path.isfile(source):
            destination = os.path.join(target, os.path.basename(source))
            shutil.copy2(source, destination)
            copied.append(destination)
    _record('backup', files=copied)
    return target


def delete_duplicate(path, expected_sha256, library_paths):
    roots = _roots(library_paths)
    if not _inside(path, roots) or not os.path.isfile(path):
        raise ValueError('The duplicate path is outside the configured libraries or does not exist.')
    actual = sha256_file(path)
    if actual != expected_sha256:
        raise ValueError('The file changed since the preview; it was not deleted.')
    os.remove(path)
    return record_delete(path, actual)


def maintenance_report(library_paths):
    roots = _roots(library_paths)
    tracked = 0
    missing = 0
    empty_dirs = 0
    for root in roots:
        for dirpath, dirnames, filenames in os.walk(root):
            if os.path.abspath(dirpath) != root and not dirnames and not filenames:
                empty_dirs += 1
            tracked += len(filenames)
    try:
        from db import Files
        tracked_rows = Files.query.all()
        missing_tracked = sum(not os.path.exists(row.filepath) for row in tracked_rows)
        unidentified = sum(not row.identified for row in tracked_rows)
    except Exception:
        # The report is also useful during first-run/bootstrap, before the ORM has
        # been initialized, so filesystem facts remain available on their own.
        missing_tracked = 0
        unidentified = 0
    return {
        'libraries': len(roots),
        'files_on_disk': tracked,
        'tracked_files_missing': missing_tracked,
        'unidentified_files': unidentified,
        'missing_directories': missing,
        'empty_directories': empty_dirs,
        'duplicate_groups': len(find_duplicate_groups(roots)),
        'changes': list_changes(20),
    }
