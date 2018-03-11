
from requests import Request
from requests import Session as Session_

HEADERS = {"X-Requested-With": "python-3x/api"}
API_V2 = ""

class APISession:

    def __init__(self, username, password, host):
        self.host = host
        self.session = Session_()
        self.session.auth = (username, password)
        self.session.headers.update(HEADERS)

    def post(self, uri, data):
        url = self.host + uri
        return (url, data)

    def get(self, url, data):
        pass
        
    def put(self, url, data):
        pass

    def delete(self, url):
        pass


