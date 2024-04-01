#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of the 
response (decoded in utf-8). If the request fails, displays an error response.

"""
import sys
import requests

if __name__ == "__main__":
    URL = sys.argv[1]
    RESULT = requests.get(URL, timeout=5)
    if RESULT.status_code >= 400:
        print(f"Error code: {RESULT.status_code}")
    else:
        print(RESULT.text)
