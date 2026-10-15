#!/usr/bin/env python3

from requests import put, get

put(
    'http://localhost:5001/light1',
    data={'status': 'enabled'}
)

response = get('http://localhost:5001/light1')

print(response.json())
