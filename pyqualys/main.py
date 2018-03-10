# -*- coding: utf-8 -*-

from utils.session import Session

class QualysAPI(object):

    def __init__(self, username=None, password=None, host=None):
        if not username or not password:
            print("Error: username or password missing.")
        elif not host:
            print("Error: host parameter is missing.")
        super(Session).__init__(username=username, password=password, host=host)

    def list_services(self):
        return self.services

    def service(self, service_name):
        if service_name not in self.services:
            print("Service is not available.")

        if service_name == "vulnerbility":
            from services.vulnerbility import Service
            return Service(self.session) # Return object

