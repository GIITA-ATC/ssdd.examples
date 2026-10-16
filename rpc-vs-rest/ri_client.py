import requests

url = 'http://localhost:5001/devices/door1'

print(requests.put(url,
    json={'operation': 'open', 'args': [20]}).json())

print(requests.put(url,
    json={'operation': 'getOpening', 'args': []}).json())
