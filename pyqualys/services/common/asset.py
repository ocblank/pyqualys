
from collections import defaultdict

class AssetHandler:

    def __init__(self, session, api_version, urls_map):
        self.session = session
        self.api_version = api_version
        self.urls_map = urls_map

    def add_asset(self, title, ip):
        data = defaultdict(str)
        data["action"] =  "add"
        data["title"] =  title
        data["ip"] =  ip
        uri = self.api_version + self.urls_map.add
        resp = self.session.post(uri, data)
        return resp

    def edit_asset(self):
        pass

    def delete_asset(self):
        pass

    def get_asset(self):
        pass
