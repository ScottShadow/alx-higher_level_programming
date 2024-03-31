#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.

"""

import sys
from json import JSONDecodeError
import requests
q = "" if len(sys.argv) < 2 else sys.argv[1]
URL = 'http://0.0.0.0:5000/search_user'
DATA = {'q': q}
RESULT = requests.post(URL, data=DATA, timeout=5)

try:
    RESULT_JSON = RESULT.json()
    if RESULT_JSON:
        print(f"[{RESULT_JSON['id']}] {RESULT_JSON['name']}")
    else:
        print("No result")
except JSONDecodeError as e:
    print("Not a valid JSON")
