"""LAN discovery responder for Sphaira's Ownfoil server search."""
import json
import logging
import socket
import threading

from constants import (
    APP_VERSION, DISCOVERY_MAGIC, DISCOVERY_PORT, DISCOVERY_REQUEST, HTTP_PORT,
)
from settings import get_server_uid, get_settings

logger = logging.getLogger('main')

_responder = None
_lock = threading.Lock()


def discovery_payload():
    """Return the server identity and addresses advertised to LAN clients."""
    shop = get_settings()['shop']
    return {
        'magic': DISCOVERY_MAGIC,
        'uid': get_server_uid(),
        'name': shop['name'],
        'version': APP_VERSION,
        'port': HTTP_PORT,
        'remote': shop['host'],
        'public': shop['public'],
    }


class DiscoveryResponder(threading.Thread):
    """Answer the UDP broadcast requests sent by Sphaira on the local network."""

    def __init__(self, port=DISCOVERY_PORT):
        super().__init__(daemon=True)
        self.port = port
        self.sock = None
        self._stopping = False

    def bind(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.bind(('', self.port))
        except OSError as error:
            sock.close()
            logger.warning('LAN discovery disabled: cannot listen on UDP port %s (%s).',
                           self.port, error)
            return False
        self.sock = sock
        self.port = sock.getsockname()[1]
        return True

    def run(self):
        while not self._stopping:
            try:
                message, sender = self.sock.recvfrom(1024)
            except OSError:
                break
            if message.strip() != DISCOVERY_REQUEST:
                continue
            try:
                self.sock.sendto(json.dumps(discovery_payload()).encode(), sender)
            except OSError as error:
                logger.warning('Could not answer discovery request from %s: %s',
                               sender[0], error)

    def stop(self):
        self._stopping = True
        self.sock.close()
        self.join(timeout=5)


def reconcile():
    """Ensure the discovery responder is running."""
    global _responder
    with _lock:
        if _responder is None:
            responder = DiscoveryResponder()
            if responder.bind():
                responder.start()
                _responder = responder
                logger.info('LAN discovery listening on UDP port %s.', responder.port)


def stop():
    """Stop the responder during worker shutdown."""
    global _responder
    with _lock:
        if _responder is not None:
            _responder.stop()
            _responder = None
