
import pyqualys

obj = pyqualys.QualysAPI(username="admin", password="admin", host="http://qualysapi.com/")

service = obj.service("vulnerability")

# Add asset
request = service.add_asset(title="Linux", ip="10.0.0.1-50")
print("Response", request)
