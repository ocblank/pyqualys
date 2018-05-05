
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

    def add_asset(self, **kwargs):
        if "title" not in kwargs and "ip" not in kwargs:
            print("ip or title is missing.")
        data = kwargs
        data["action"] = "add"
        uri = self.asset_api_version + self.asset_urls_map
        resp = self.session.post(uri, data)
        print(resp.text)
        x = resp # ScanAsset(id=resp["id"])
        return x

    def update_asset(self, **kwargs):
        print("Updating Asset", kwargs)
        if "asset_id" not in kwargs or "id" not in kwargs:
            print("asset_id or id is missing.")
            return
        if "asset_id" in kwargs:
            kwargs["id"] = kwargs.pop("asset_id")
        data = kwargs
        data["action"] = "edit"

        uri = self.asset_api_version + self.asset_urls_map
        resp = self.session.post(uri, data)
        print(resp.text)
        return resp

    def delete_asset(self, asset_id):
        print("Deleting Asset", asset_id)
        data = {"action": "delete", "id": asset_id}

        uri = self.asset_api_version + self.asset_urls_map
        resp = self.session.post(uri, data)
        print(resp.text)
        return resp

    def list_assets(self):
        print("List of the Asset")
        data = {"action": "list", "show_attributes": "ALL"}

        uri = self.asset_api_version + self.asset_urls_map
        resp = self.session.post(uri, data)
        for line in resp.text:
            if line.find("myLinux") != -1:
                print(line)
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