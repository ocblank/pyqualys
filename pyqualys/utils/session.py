# -*- coding: utf-8 -*-
import logging
from requests import Request
from requests import Session

logger = logging.getLogger(__name__)
HEADERS = {"X-Requested-With": "pyqualys/python-3x"}

class APISession(object):

    def __init__(self, username, password, host):
        self.__host = host
        self.__session = Session()
        self.__session.auth = (username, password)
        self.__session.headers.update(HEADERS)

    def post(self, uri, data):
        url = self.__host + uri
        logger.debug(url, data)
        resp = self.__session.post(url, data=data, verify=False)
        return resp

    def get(self, uri, data):
        url = self.__host + uri
        logger.debug(url, data)
        resp = self.__session.get(url, data=data, verify=False)
        return resp
        
    def put(self, uri, data):
        url = self.__host + uri
        logger.debug(url, data)
        resp = self.__session.put(url, data=data, verify=False)
        return resp

    def delete(self, uri, data):
        url = self.__host + uri
        logger.debug(url, data)
        resp = self.__session.delete(url, data=data, verify=False)
        return resp


