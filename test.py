import requests

BASE = "http://127.0.0.1:5000/"

response = requests.patch(BASE + "video/1", {"views": 9298388})
print(response.json())