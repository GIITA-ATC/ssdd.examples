import requests

url = 'http://localhost:5001/devices/door1'
print(requests.put(url, json={'percentage_open': 20}).json())
print(requests.get(url).json())
