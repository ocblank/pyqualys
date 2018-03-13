
class UserHandler:

    def __init__(self, session, api_version, urls_map):
        self.session = session
        self.api_version = api_version
        self.urls_map = urls_map

    def add_user(self, **data):
        data["action"] = "add"
        uri = self.api_version + self.urls_map.user
        resp = self.session.post(uri, data)
        return resp

    def edit_user(self, **parameter):
        pass

    def delete_user(self):
        pass

    def get_user(self):
        pass

    def search_user(self, **kwags):
        pass