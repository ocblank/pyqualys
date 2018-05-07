
import pyqualys

obj = pyqualys.QualysAPI(username="admin", password="admin", host="https://qualys.com/")

service = obj.service("vulnerability")


# Add asset
# asset = service.add_asset(title="myLinux", ips="10.10.10.1")
# print("Add asset Response", asset)

# Update asset
# asset = service.update_asset(asset_id=306065, title="myOS", ips="10.10.10.1")
# print("Update asset Response", asset)


# # Delete asset
# asset = service.delete_asset(asset_id=306065)
# print("Delete asset Response", asset)

# # List of assets
# assets = service.list_assets()
# print("List asset Response", assets)

# # Get asset
# asset = service.search_asset(asset_id=306065)
# print("Get asset Response", asset)

# List of Scan
# scan = asset.scan_list()
# print(scan)

# Start Scan
# scan = asset.start_scan(scan_title="MyScan", ip="10.10.10.1", iscanner_name="mytest", option_title="Initial Options")


# # Add user
# info = {}
# info["business_unit"] = "my Business"

# info["first_name"] = "Amit"
# info["last_name"] = "Ghadge"
# info["phone"] = "1234567890"
# info["email"] = "hello@qualys.com"

# user = service.add_user(data=info, acceptEULA=True)
# user.acceptEULA = True
# user.acceptEULA()

# # print("Response", request)
# # request = service.get_asset()
# # print("Response", request)
# # scan = asset.scan_asset()