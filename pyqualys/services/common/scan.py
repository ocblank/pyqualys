# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)


class ScanAsset(object):
    def __init__(self, **kwargs):
        self.endpoint = kwargs.pop('endpoint')
        self.uri = kwargs.pop('uri')
        self.session = kwargs.pop('session')
            
    def scan_list(self, **kwargs):
        data = kwargs
        data["action"] = "list"
        resp = self.session.post(self.endpoint+self.uri.scan, data)
        return resp

    def start_scan(self, **kwargs):
        data = kwargs
        data["action"] = "launch"
        resp = self.session.post(self.endpoint+self.uri.scan, data)
        return resp

    def manage_scan(self, **kwargs):
        data = kwargs
        resp = self.session.post(self.endpoint+self.uri.scan, data)
        return resp

    def get_scan_report(self, **kwargs):
        data = kwargs
        data["action"] = "fetch"
        resp = self.session.post(self.endpoint+self.uri.scan, data)
        return resp


def scanner(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        info = result["info"]
        # obj = result["obj"]
        print(info)
        return ScanAsset(endpoint=info["endpoint"], uri=info["uri"],
                         session=info["session"])
    return inner
