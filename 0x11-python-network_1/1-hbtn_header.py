#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
found in the header of the response
"""
import sys
import urllib.request


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.getheader('X-Request-Id'))
