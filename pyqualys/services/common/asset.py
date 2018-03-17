


class AssetHandler(object):

    def __init__(self, session, api_version, urls_map):
        self.session = session
        self.asset_api_version = api_version
        self.asset_urls_map = urls_map.asset
        super(AssetHandler, self).__init__(session, api_version, urls_map)

    def add_asset(self, title, ip):
        data = {"action": "add", "title": title, "ips": ip}
        uri = self.asset_api_version + self.asset_urls_map
        resp = self.session.post(uri, data)
        return resp

    def edit_asset(self, **parameter):
        pass

    def delete_asset(self):
        pass

    def get_assets(self):
        data = {"action": "list", "show_attributes": "ALL"}
        uri = self.asset_api_version + self.asset_urls_map.asset
        resp = self.session.post(uri, data)
        with open("tmp.txt", "w") as awrite:
            awrite.writelines(str(resp.text)) 
        return True

    def search_asset(self, **kwargs):
        query_title = kwargs.get('title')
        query_ip = kwargs.get('ip')
