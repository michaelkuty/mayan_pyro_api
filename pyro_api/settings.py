# -*- coding: utf-8 -*-

SERVER_IP = "192.168.23.7"
DAEMON_NAME = "document_api"
NS_BCHOST = "mayan.coex.cz"
HMAC_KEY = "d2d00896183011e28eb950e5493b2d90"

try:
    from settings_local import *
except ImportError:
    pass