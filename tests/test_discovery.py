import base64
import json
import socket

import pytest

import discovery
from constants import (
    APP_VERSION, DISCOVERY_MAGIC, DISCOVERY_REQUEST, HTTP_PORT,
)
from settings import get_server_uid, set_shop_settings
from db import Files, db


def test_discovery_responder_answers_sphaira_broadcast(shop_app):
    responder = discovery.DiscoveryResponder(port=0)
    assert responder.bind()
    responder.start()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
            client.settimeout(2)
            client.sendto(DISCOVERY_REQUEST, ("127.0.0.1", responder.port))
            data, _ = client.recvfrom(1024)
    finally:
        responder.stop()

    payload = json.loads(data)
    assert payload == {
        "magic": DISCOVERY_MAGIC,
        "uid": get_server_uid(),
        "name": "NS eShop Server",
        "version": APP_VERSION,
        "port": HTTP_PORT,
        "remote": "",
        "public": False,
    }


def test_ownfoil_handshake_returns_server_identity(shop_app):
    set_shop_settings({"public": True, "name": "My Shop", "motd": "Hello"})

    response = shop_app.client.open("/", method="OPTIONS")

    assert response.status_code == 200
    assert response.json == {
        "uid": get_server_uid(),
        "name": "My Shop",
        "version": APP_VERSION,
        "protocol_version": 1,
        "motd": "Hello",
        "public": True,
        "remote": "",
        "features": {
            "shop": True,
            "resumable_download": True,
            "dumps_upload": False,
            "save_backup": False,
            "resumable_upload": False,
        },
    }


def test_ownfoil_handshake_accepts_basic_auth_for_private_shop(shop_app):
    set_shop_settings({"public": False})
    credentials = base64.b64encode(b"shopper:shoppass1").decode()

    response = shop_app.client.open(
        "/", method="OPTIONS", headers={"Authorization": f"Basic {credentials}"})

    assert response.status_code == 200
    assert response.json["uid"] == get_server_uid()


def test_ownfoil_handshake_requires_shop_access(shop_app):
    set_shop_settings({"public": False})

    response = shop_app.client.open("/", method="OPTIONS")

    assert response.status_code == 401
    assert response.headers["WWW-Authenticate"].startswith("Basic ")


@pytest.mark.parametrize("query", [
    """query { apps(owned: true, appType: [BASE], groupByAppId: true,
                   page: 1, pageSize: 20) {
        total items { appId titleId appVersion displayVersion
          latestOwnedVersion { displayVersion } downloadUrl downloadSize downloadExtension
          titledb { name publisher icon(size: THUMB) { url local }
                    banner(size: THUMB) { url local } }
        }
    } }""",
    """query($id: ID!) { title(titleId: $id) {
        name publisher intro description releaseDate category numberOfPlayers size rating region
        banner(size: CLIENT) { url local }
        fullBanner: banner(size: SCREEN) { url local }
        availableVersions { version releaseDate }
        screenshots(size: CLIENT) { url local }
        full: screenshots(size: SCREEN) { url local }
        base: apps(owned: true, appType: [BASE]) {
          displayVersion downloadSize downloadUrl downloadExtension
          latestOwnedVersion { version displayVersion }
        }
        updates: apps(owned: true, appType: [UPDATE]) {
          appVersion displayVersion downloadUrl downloadExtension
        }
        dlc: apps(owned: true, appType: [DLC]) {
          appId appVersion downloadUrl downloadExtension
          titledb { name intro banner(size: THUMB) { url local } }
        }
    } }""",
    """query($page: Int!, $pageSize: Int!, $appIds: [String!]) {
        apps(owned: true, appType: [BASE], groupByAppId: true,
             filter: {appId: {notIn: $appIds}}, page: $page, pageSize: $pageSize) {
            total items { appId }
        }
    }""",
])
def test_graphql_accepts_sphaira_catalog_queries(shop_app, query):
    set_shop_settings({"public": True})

    response = shop_app.client.post(
        "/api/graphql",
        json={"query": query, "variables": {
            "id": "0100000000001000", "page": 1, "pageSize": 20, "appIds": []}},
    )

    assert response.status_code == 200
    assert "errors" not in response.json


def test_graphql_shop_queries_accept_basic_auth(shop_app):
    set_shop_settings({"public": False})
    credentials = base64.b64encode(b"shopper:shoppass1").decode()

    response = shop_app.client.post(
        "/api/graphql",
        json={"query": "{ apps(owned: true) { total items { appId } } }"},
        headers={"Authorization": f"Basic {credentials}"},
    )

    assert response.status_code == 200
    assert "errors" not in response.json


def test_sphaira_download_fields_resolve_to_existing_file(shop_app):
    set_shop_settings({"public": True})
    query = """{
        apps(owned: true, appType: [BASE], groupByAppId: true) {
            items { downloadUrl downloadSize downloadExtension }
        }
    }"""
    response = shop_app.client.post("/api/graphql", json={"query": query})

    assert response.status_code == 200
    app = response.json["data"]["apps"]["items"][0]
    assert app["downloadUrl"] == "/api/get_game/1"
    assert app["downloadSize"] == 4096
    assert app["downloadExtension"] == "nsp"

    download = shop_app.client.get(app["downloadUrl"])
    assert download.status_code == 200
    assert len(download.data) == 4096

    ranged_download = shop_app.client.get(
        app["downloadUrl"], headers={"Range": "bytes=0-15"})
    assert ranged_download.status_code == 206
    assert ranged_download.headers["Content-Range"] == "bytes 0-15/4096"
    assert len(ranged_download.data) == 16


def test_sphaira_download_size_supports_files_larger_than_graphql_int(shop_app):
    set_shop_settings({"public": True})
    large_size = 12_752_574_567
    with shop_app.app.app_context():
        file = Files.query.filter_by(id=1).one()
        file.size = large_size
        db.session.commit()

    response = shop_app.client.post(
        "/api/graphql",
        json={"query": """{
            title(titleId: "0100000000010000") {
                base: apps(owned: true, appType: [BASE]) {
                    downloadSize downloadUrl
                }
                updates: apps(owned: true, appType: [UPDATE]) {
                    downloadSize downloadUrl
                }
                dlc: apps(owned: true, appType: [DLC]) {
                    downloadSize downloadUrl
                }
            }
        }"""},
    )

    assert response.status_code == 200
    assert "errors" not in response.json, response.json
    title = response.json["data"]["title"]
    assert title["base"][0]["downloadSize"] == large_size
