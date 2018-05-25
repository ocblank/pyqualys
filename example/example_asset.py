# -*- coding: utf-8 -*-
import re
import pyqualys

obj = pyqualys.QualysAPI(username="admin",
                         password="admin",
                         host="https://qualys.com/")

service = obj.service("vulnerability")


# Add asset
asset = service.add_asset(title="myLinux", ips="10.10.10.1")
print("Add asset Response", asset)
response = asset.response['data']['RESPONSE']
asset_id = response['ITEM_LIST']['ITEM']['VALUE']


# # Update asset
asset = service.update_asset(asset_id=asset_id, title="myOS", ips="10.10.10.1")
print("Update asset Response", asset)


# # List of assets
assets = service.list_assets()
print("List asset Response", assets)


# # Get asset
asset = service.search_asset(ids=asset_id)
print("Get asset Response", asset)


# # Delete asset
asset = service.delete_asset(asset_id=asset_id)
print("Delete asset Response", asset)
