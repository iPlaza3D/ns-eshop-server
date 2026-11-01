"""Safe, small on-disk cache for catalogue artwork.

The Switch client receives artwork URLs from the server and caches them locally.
The browser should get the same server-owned behaviour so an external CDN outage
does not turn every DLC row into a missing image.
"""

import hashlib
import mimetypes
import os
import tempfile
from dataclasses import dataclass
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from constants import DATA_DIR


ARTWORK_CACHE_DIR = os.path.join(DATA_DIR, 'artwork-cache')
ARTWORK_MAX_BYTES = 10 * 1024 * 1024
ARTWORK_HOSTS = frozenset({
    'img-eshop.cdn.nintendo.net',
})


@dataclass(frozen=True)
class CachedArtwork:
    path: str
    content_type: str


def _validate_url(url: str) -> tuple[str, str]:
    parsed = urlparse(url)
    host = (parsed.hostname or '').lower()
    if parsed.scheme not in {'http', 'https'} or host not in ARTWORK_HOSTS:
        raise ValueError('Artwork URL is not from an allowed catalogue host.')
    return url, host


def _cache_path(url: str, content_type: str = '') -> str:
    digest = hashlib.sha256(url.encode('utf-8')).hexdigest()
    extension = os.path.splitext(urlparse(url).path)[1].lower()
    if extension not in {'.jpg', '.jpeg', '.png', '.webp'}:
        extension = mimetypes.guess_extension(content_type.split(';', 1)[0]) or '.img'
    return os.path.join(ARTWORK_CACHE_DIR, digest + extension)


def get_cached_artwork(url: str) -> CachedArtwork:
    """Return a cached artwork file, downloading it once from an allow-listed CDN."""
    url, _ = _validate_url(url)
    os.makedirs(ARTWORK_CACHE_DIR, exist_ok=True)

    # Most TitleDB URLs already carry their image extension, so this fast path avoids
    # a network request and also preserves the upstream content type.
    for extension in ('.jpg', '.jpeg', '.png', '.webp', '.img'):
        candidate = os.path.join(
            ARTWORK_CACHE_DIR,
            hashlib.sha256(url.encode('utf-8')).hexdigest() + extension,
        )
        if os.path.isfile(candidate):
            return CachedArtwork(candidate, mimetypes.guess_type(candidate)[0] or 'image/jpeg')

    request = Request(url, headers={'User-Agent': 'NS-eShop-Server artwork cache'})
    with urlopen(request, timeout=15) as response:
        content_type = response.headers.get_content_type() or 'image/jpeg'
        content_length = response.headers.get('Content-Length')
        if content_length and int(content_length) > ARTWORK_MAX_BYTES:
            raise ValueError('Artwork response is too large.')
        data = response.read(ARTWORK_MAX_BYTES + 1)
        if len(data) > ARTWORK_MAX_BYTES:
            raise ValueError('Artwork response is too large.')

    destination = _cache_path(url, content_type)
    fd, temporary = tempfile.mkstemp(prefix='.artwork-', dir=ARTWORK_CACHE_DIR)
    try:
        with os.fdopen(fd, 'wb') as output:
            output.write(data)
        os.replace(temporary, destination)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return CachedArtwork(destination, content_type)
