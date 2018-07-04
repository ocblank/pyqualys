# -*- coding: utf-8 -*-
import re
import pyqualys

obj = pyqualys.QualysAPI(username="admin", password="admin@1",
                         host="https://qualys.com/")

# service = obj.service("vulnerability")
# print(id(service))
service = obj.service("assetview")

# service.create_tag(parameter)
# service.FORMAT = "xml"

# Add asset
# asset = service.add_asset(title="myLinux01", ips="10.10.10.11")
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

# asset = service.search_asset(ids=311275)
# print("Get asset Response", asset.response['data']['RESPONSE'])


# List of Scan
# scan = asset.scan_list()
# print(scan)

# Start Scan
# scan = asset.start_scan(scan_title="MyLinuxScanTest",
#                         iscanner_name="mytest",
#                         option_title="Initial Options")
# print("Start Scan", scan.text)

# OR

# Start Scan
# scan = service.scanner.start_scan(scan_title="MyLinuxScanTest", ip="10.114.26.122",
#                                   iscanner_name="AGScan",
#                                   option_title="Initial Options")

# Get Scan Report
#
# # Get report the scanner
# report = asset.get_scan_report(echo_request=1,
#                                scan_ref="scan/1525944287.01369",
#                                output_format="json")

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
