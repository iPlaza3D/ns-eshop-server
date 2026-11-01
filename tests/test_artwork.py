import hashlib

import pytest

import artwork


def test_artwork_rejects_untrusted_hosts():
    with pytest.raises(ValueError):
        artwork.get_cached_artwork('http://127.0.0.1/private.png')


def test_artwork_reuses_cached_file(tmp_path, monkeypatch):
    url = 'https://img-eshop.cdn.nintendo.net/i/example.jpg'
    monkeypatch.setattr(artwork, 'ARTWORK_CACHE_DIR', str(tmp_path))
    path = tmp_path / (hashlib.sha256(url.encode('utf-8')).hexdigest() + '.jpg')
    path.write_bytes(b'cached')

    result = artwork.get_cached_artwork(url)

    assert result.path == str(path)
    assert result.content_type == 'image/jpeg'
