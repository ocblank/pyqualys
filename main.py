
import pyqualys

obj = pyqualys.QualysAPI(username="admin", password="admin", host="https://qualys.com/")

service = obj.service("vulnerability")

# Add asset
# request = service.add_asset(title="Linux", ip="13.255.255.255")
# print("Response", request)

# Add user
info = {}
info["business_unit"] = "my Business"
info["first_name"] = "User1"

info["last_name"] = "Lastename"
info["phone"] = "1234567890"
info["email"] = "hello@qualys.com"
# request = service.add_user(data=info)
# print("Response", request)

request = service.get_asset()
print("Response", request)
