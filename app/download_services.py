"""Small adapters for Jackett and Synology Download Station."""

import requests

from settings import get_settings


class DownloadServiceError(RuntimeError):
    """An external download service could not complete the requested action."""


def _service(name):
    config = get_settings().get('downloads', {}).get(name, {})
    if not config.get('enabled'):
        raise DownloadServiceError(f'{name} is disabled in the server settings.')
    if not config.get('url'):
        raise DownloadServiceError(f'{name} has no URL configured.')
    return config


def _webapi_url(base_url, path):
    base = base_url.rstrip('/')
    if not base.endswith('/webapi'):
        base += '/webapi'
    return f'{base}/{path.lstrip("/")}'


def search_jackett(query):
    """Search Jackett and return only safe fields needed by the admin UI."""
    config = _service('jackett')
    query = (query or '').strip()
    if len(query) < 2:
        raise DownloadServiceError('The search query must contain at least 2 characters.')

    response = requests.get(
        f"{config['url'].rstrip('/')}/api/v2.0/indexers/all/results/torznab/api",
        params={'apikey': config.get('api_key', ''), 'q': query},
        timeout=20,
    )
    response.raise_for_status()
    payload = response.json()
    results = payload.get('Results', []) if isinstance(payload, dict) else []
    normalized = []
    for result in results[:50]:
        uri = result.get('MagnetUri') or result.get('Link') or result.get('Guid')
        if not uri:
            continue
        normalized.append({
            'title': result.get('Title') or 'Untitled result',
            'uri': uri,
            'size': result.get('Size'),
            'seeders': result.get('Seeders'),
            'indexer': result.get('Tracker') or result.get('Indexer'),
        })
    return normalized


def add_to_download_station(uri):
    """Authenticate and enqueue a magnet/torrent URI in Download Station."""
    config = _service('download_station')
    uri = (uri or '').strip()
    if not uri or not (uri.startswith('magnet:') or uri.startswith('http://') or uri.startswith('https://')):
        raise DownloadServiceError('The selected result does not contain a valid download URI.')

    auth_params = {
        'api': 'SYNO.API.Auth',
        'version': 6,
        'method': 'login',
        'account': config.get('username', ''),
        'passwd': config.get('password', ''),
        'session': 'DownloadStation',
        'format': 'sid',
    }
    auth = requests.get(_webapi_url(config['url'], 'auth.cgi'), params=auth_params, timeout=20).json()
    if not auth.get('success'):
        raise DownloadServiceError('Download Station rejected the configured credentials.')

    sid = auth['data']['sid']
    try:
        created = requests.get(
            _webapi_url(config['url'], 'DownloadStation/task.cgi'),
            params={
                'api': 'SYNO.DownloadStation.Task',
                'version': 3,
                'method': 'create',
                'uri': uri,
                '_sid': sid,
            },
            timeout=20,
        ).json()
        if not created.get('success'):
            raise DownloadServiceError('Download Station could not create the task.')
        return created.get('data', {})
    finally:
        try:
            requests.get(
                _webapi_url(config['url'], 'auth.cgi'),
                params={'api': 'SYNO.API.Auth', 'version': 6, 'method': 'logout', 'session': 'DownloadStation', '_sid': sid},
                timeout=10,
            )
        except requests.RequestException:
            pass
