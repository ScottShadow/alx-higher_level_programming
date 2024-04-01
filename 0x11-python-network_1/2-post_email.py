#!/usr/bin/python3
"""
POST request to the passed URL with the email as a parameter
"""
import sys
import urllib.request


if __name__ == "__main__":
    URL = sys.argv[1]
    EMAIL = sys.argv[2]
    try:
        DATA = urllib.parse.urlencode({'email': EMAIL}).encode('ascii')
        REQ = urllib.request.Request(URL, DATA, method="POST")
        with urllib.request.urlopen(REQ) as response:
            print(response.read().decode('utf-8'))
    except Exception as e:
        print("Error:", e)
