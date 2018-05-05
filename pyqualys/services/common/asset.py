
from .scan import ScanAsset

class AssetHandler(object):

    def __init__(self, session, api_version, urls_map):
        self.session = session
        self.asset_api_version = api_version
        self.asset_urls_map = urls_map.asset
        super(AssetHandler, self).__init__(session=session,
                                            api_version=api_version,
                                            urls_map=urls_map)
    def get_asset_obj(self):
        pass

    def add_asset(self, *args, **kwargs):
        title = kwargs.get("title")
        ip = kwargs.get("ip")
        data = {"action": "add", "title": title, "ips": ip}
        uri = self.asset_api_version + self.asset_urls_map
        resp = self.session.post(uri, data)
        x = ScanAsset(id=resp["id"])
        return x

    def update_asset(self, **kwargs):
        print("Updating Asset", kwargs)
        if "asset_id" not in kwargs:
            print("Pass asset id")
        data = kwargs.copy()
        data["action"] = "edit"
        data["id"] = data["asset_id"]

        uri = self.asset_api_version + self.asset_urls_map
        resp = self.session.put(uri, data)
        return resp

    def delete_asset(self, asset_id):
        print("Deleting Asset", asset_id)
        data = {"action": "delete", "id": asset_id}

        uri = self.asset_api_version + self.asset_urls_map
        resp = self.session.delete(uri, data)
        return resp

    def list_assets(self):
        print("List of the Asset")
        data = {"action": "list", "show_attributes": "ALL"}

        uri = self.asset_api_version + self.asset_urls_map
        resp = self.session.post(uri, data)
        return resp

    def search_asset(self, **kwargs):
        print("Search the asset", kwargs)
        query_title = kwargs.get('title')
        query_ip = kwargs.get('ip')
        data = kwargs.copy()
        data["action"] = "search"

        uri = self.asset_api_version + self.asset_urls_map
        resp = self.session.post(uri, data)
        return resp