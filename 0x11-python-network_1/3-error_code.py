#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""
import sys
import urllib.request

URL = sys.argv[1]
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(URL) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    except Exception as e:
        print(f"Error code: {e}")
