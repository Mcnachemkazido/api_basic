import requests

data = {"price":20}

url = "http://localhost:8000/items/1"
rec = requests.put(url,json=data)

print(rec.status_code)
print(rec.json())