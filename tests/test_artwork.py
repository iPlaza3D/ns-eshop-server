import hashlib
import types

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


def test_file_access_accepts_authenticated_web_session(monkeypatch):
    import app as app_module

    user = types.SimpleNamespace(
        user='web-user',
        has_shop_access=lambda: True,
    )
    session_user = types.SimpleNamespace(
        is_authenticated=True,
        _get_current_object=lambda: user,
    )
    monkeypatch.setattr(app_module, 'get_settings', lambda: {'shop': {'public': False}})
    monkeypatch.setattr(app_module, 'current_user', session_user)

    @app_module.file_access
    def protected_endpoint():
        return 'ok'

    with app_module.app.test_request_context('/api/artwork'):
        assert protected_endpoint() == 'ok'
