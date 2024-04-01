#!/usr/bin/python3
"""
POST request to the passed URL with the email as a parameter
"""
import sys
import urllib.request

URL = sys.argv[1]
EMAIL = sys.argv[2]
DATA = urllib.parse.urlencode({'email': EMAIL}).encode('ascii')
REQ = urllib.request.Request(URL, DATA, method="POST")
if __name__ == "__main__":
    with urllib.request.urlopen(REQ) as response:
        print(response.read().decode('utf-8'))
