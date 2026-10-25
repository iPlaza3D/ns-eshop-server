"""Small adapters for Jackett and Synology Download Station."""

import requests
from xml.etree import ElementTree

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
        params={'apikey': config.get('api_key', ''), 't': 'search', 'q': query},
        timeout=20,
    )
    response.raise_for_status()
    try:
        payload = response.json()
        results = payload.get('Results', []) if isinstance(payload, dict) else []
    except ValueError:
        # Torznab commonly returns RSS/XML unless the Jackett build is configured
        # for JSON. Keep both formats working across Jackett versions.
        root = ElementTree.fromstring(response.text)
        results = []
        for item in root.findall('.//item'):
            attrs = {node.attrib.get('name'): node.attrib.get('value') for node in item.findall('{*}attr')}
            results.append({
                'Title': item.findtext('title'),
                'Link': item.findtext('link'),
                'Guid': item.findtext('guid'),
                'Size': attrs.get('size'),
                'Seeders': attrs.get('seeders'),
                'Tracker': attrs.get('tracker'),
            })
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


def test_jackett():
    """Verify that Jackett accepts the configured API key."""
    config = _service('jackett')
    response = requests.get(
        f"{config['url'].rstrip('/')}/api/v2.0/indexers/all/results/torznab/api",
        params={'apikey': config.get('api_key', ''), 't': 'search', 'q': 'Nintendo'},
        timeout=20,
    )
    response.raise_for_status()
    try:
        payload = response.json()
        if not isinstance(payload, dict) or 'Results' not in payload:
            raise DownloadServiceError('Jackett returned an invalid response.')
        return {'results': len(payload['Results'])}
    except ValueError:
        try:
            root = ElementTree.fromstring(response.text)
            return {'results': len(root.findall('.//item'))}
        except ElementTree.ParseError as error:
            raise DownloadServiceError('Jackett returned an invalid response.') from error


def _login_download_station(config):
    auth = requests.get(
        _webapi_url(config['url'], 'auth.cgi'),
        params={
            'api': 'SYNO.API.Auth',
            'version': 6,
            'method': 'login',
            'account': config.get('username', ''),
            'passwd': config.get('password', ''),
            'session': 'DownloadStation',
            'format': 'sid',
        },
        timeout=20,
    ).json()
    if not auth.get('success'):
        raise DownloadServiceError('Download Station rejected the configured credentials.')
    return auth['data']['sid']


def test_download_station():
    """Verify credentials without creating a download task."""
    config = _service('download_station')
    sid = _login_download_station(config)
    try:
        return {'connected': True}
    finally:
        try:
            requests.get(
                _webapi_url(config['url'], 'auth.cgi'),
                params={'api': 'SYNO.API.Auth', 'version': 6, 'method': 'logout', 'session': 'DownloadStation', '_sid': sid},
                timeout=10,
            )
        except requests.RequestException:
            pass


def add_to_download_station(uri):
    """Authenticate and enqueue a magnet/torrent URI in Download Station."""
    config = _service('download_station')
    uri = (uri or '').strip()
    if not uri or not (uri.startswith('magnet:') or uri.startswith('http://') or uri.startswith('https://')):
        raise DownloadServiceError('The selected result does not contain a valid download URI.')

    sid = _login_download_station(config)
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
