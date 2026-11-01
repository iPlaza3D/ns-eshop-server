import os

import pytest

from maintenance import delete_duplicate, find_duplicate_groups, sha256_file


def test_find_duplicate_groups_is_content_based(tmp_path):
    first = tmp_path / 'first.nsp'
    second = tmp_path / 'second.nsp'
    different = tmp_path / 'different.nsp'
    first.write_bytes(b'same content')
    second.write_bytes(b'same content')
    different.write_bytes(b'not the same')

    groups = find_duplicate_groups([str(tmp_path)])

    assert len(groups) == 1
    assert groups[0]['sha256'] == sha256_file(str(first))
    assert set(groups[0]['files']) == {str(first), str(second)}
    assert groups[0]['keep'] == min(str(first), str(second))


def test_delete_duplicate_rechecks_digest_and_root(tmp_path):
    duplicate = tmp_path / 'duplicate.nsp'
    duplicate.write_bytes(b'content')

    with pytest.raises(ValueError, match='changed'):
        delete_duplicate(str(duplicate), 'wrong', [str(tmp_path)])
    assert duplicate.exists()

    event = delete_duplicate(str(duplicate), sha256_file(str(duplicate)), [str(tmp_path)])
    assert event['event'] == 'delete'
    assert not duplicate.exists()


def test_delete_duplicate_rejects_path_outside_root(tmp_path):
    outside = tmp_path.parent / 'outside.nsp'
    outside.write_bytes(b'content')
    try:
        with pytest.raises(ValueError, match='outside'):
            delete_duplicate(str(outside), sha256_file(str(outside)), [str(tmp_path)])
    finally:
        outside.unlink(missing_ok=True)
