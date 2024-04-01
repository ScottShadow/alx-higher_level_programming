#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.

"""

import sys
from json import JSONDecodeError
import requests
if __name__ == "__main__":
    q = "" if len(sys.argv) < 2 else sys.argv[1]
    URL = 'http://0.0.0.0:5000/search_user'
    DATA = {'q': q}

    try:
        RESULT = requests.post(URL, data=DATA, timeout=5)
        RESULT_JSON = RESULT.json()
        if RESULT_JSON:
            print(f"[{RESULT_JSON.get('id')}] {RESULT_JSON.get('name')}")
        else:
            print("No result")
    except JSONDecodeError:
        print("Not a valid JSON")
    except Exception as e:
        print(f"Error code: {e}")
