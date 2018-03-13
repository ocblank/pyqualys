
from requests import Request
from requests import Session

HEADERS = {"X-Requested-With": "python-3x/api"}
API_V2 = ""

class APISession:

    def __init__(self, username, password, host):
        self.__host = host
        self.__session = Session()
        self.__session.auth = (username, password)
        self.__session.headers.update(HEADERS)

    def post(self, uri, data):
        url = self.__host + uri
        print(url, data)
        resp = self.__session.post(url, data=data, verify=False)
        return resp

    def get(self, uri, data):
        url = self.__host + uri
        print(url, data)
        resp = self.__session.get(url, data=data, verify=False)
        return resp
        
    def put(self, url, data):
        pass

    def delete(self, url):
        pass


