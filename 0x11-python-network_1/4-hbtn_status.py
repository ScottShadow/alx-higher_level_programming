#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status using requests module
"""
import requests
URL = 'https://alx-intranet.hbtn.io/status'
RESULT = requests.get(URL, timeout=5)
print("Body response:")
print(f"\t- type: {type(RESULT.text)}")
print(f"\t- content: {RESULT.text}")
