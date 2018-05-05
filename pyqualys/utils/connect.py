# -*- coding: utf-8 -*-
import importlib
from .session import APISession

SERVICES = {"vulnerability": "VulnerabilityService"}

class QualysAPI(object):

    def __init__(self, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        host = kwargs.get("host")
        if not username or not password:
            print("Error: username or password missing.")
        elif not host:
            print("Error: host parameter is missing.")
        self.__session = APISession(**kwargs)

    def list_services(self):
        return SERVICES

    def service(self, service_name):
        if service_name not in SERVICES:
            print("{} Service is not available.".format(service_name))

        s = "pyqualys.services.{0}".format(service_name)
        Service = getattr(importlib.import_module(s), SERVICES[service_name])
        return Service(self.__session)

