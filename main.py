
import pyqualys

obj = pyqualys.QualysAPI(username="admin", password="admin", host="https://qualys.com/")

service = obj.service("vulnerability")


# Add asset
asset = service.add_asset(title="Linux", ip="10.0.0.1-50")
print("Add asset Response", asset)

# Update asset
# asset_ = asset.update_asset(ip="10.0.0.1-100")
asset = service.update_asset(asset_id=102, ip="10.0.0.1-100")
print("Update asset Response", asset)

# Delete asset
asset = service.delete_asset(asset_id=102)
print("Delete asset Response", asset)

# List of assets
assets = service.list_assets()
print("List asset Response", assets)

# Get asset
asset = service.search_asset(title="Linux", ip="10.0.0.1-50")
print("Get asset Response", asset)

# Add user
info = {}
info["business_unit"] = "my Business"

info["first_name"] = "Amit"
info["last_name"] = "Ghadge"
info["phone"] = "1234567890"
info["email"] = "hello@qualys.com"

user = service.add_user(data=info, acceptEULA=True)
user.acceptEULA = True
user.acceptEULA()

# print("Response", request)
# request = service.get_asset()
# print("Response", request)
# scan = asset.scan_asset()