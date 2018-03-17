


class AssetHandler(object):

    def __init__(self, session, api_version, urls_map):
        self.session = session
        self.api_version = api_version
        self.urls_map = urls_map

    def add_asset(self, title, ip):
        data = {"action": "add", "title": title, "ips": ip}
        uri = self.api_version + self.urls_map.asset
        resp = self.session.post(uri, data)
        return resp

    def edit_asset(self, **parameter):
        pass

    def delete_asset(self):
        pass

    def get_asset(self):
        data = {"action": "list", "show_attributes": "ALL"}
        uri = self.api_version + self.urls_map.asset
        resp = self.session.post(uri, data)
        with open("tmp.txt", "w") as awrite:
            awrite.writelines(str(resp.text)) 
        return True

    def search_asset(self, **kwargs):
        query_title = kwargs.get('title')
        query_ip = kwargs.get('ip')