
class ScanAsset(object):
    def __init__(self, **kwargs):
        print("Scanner", kwargs)
        self.endpoint = kwargs.pop('endpoint')
        self.session = kwargs.pop('session')

    def scan_asset(self):
        print("Scan asset here")
        pass

    def scan_list(self):
        data = {"action": "list", "echo_request":1}
        resp = self.session.post(self.endpoint, data)
        print(resp.text)

    def start_scan(self, **kwargs):
        data = kwargs
        data["action"] = "launch"
        resp = self.session.post(self.endpoint, data)
        print(resp.text)
