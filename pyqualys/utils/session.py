
from requests import Request, Session

HEADERS = {"X-Requested-With": "python-3x/api"}
API_V2 = ""

class Session:

    def __init__(self, username, password):
        self.session = Session()
        self.session.auth = (username, password)
        self.session.headers.update(HEADERS)

    def post(self, url, data):
        self.session.post(url, data)

    def get(self, url, data):
        pass
        
    def put(self, url, data):
        pass

    def delete(self, url):
        pass


