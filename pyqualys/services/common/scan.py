# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)

class ScanAsset(object):
    def __init__(self, **kwargs):
        self.endpoint = kwargs.pop('endpoint')
        self.session = kwargs.pop('session')

    def scan_list(self):
        data = {"action": "list", "echo_request":1}
        resp = self.session.post(self.endpoint, data)
        logger.info(resp.text)

    def start_scan(self, **kwargs):
        data = kwargs
        data["action"] = "launch"
        resp = self.session.post(self.endpoint, data)
        logger.info(resp.text)


def scanner(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        info = result["info"]
        return ScanAsset(endpoint=info["endpoint"], session=info["session"])
    return inner
