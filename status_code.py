import requests

req = requests.get("https://kalob.io")

print(req.status_code)