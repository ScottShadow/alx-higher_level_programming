#!/usr/bin/python3
"""
takes your GitHub credentials (username and password) and uses the GitHub API
to display your id
"""
import sys
from requests.auth import HTTPBasicAuth
import requests
if __name__ == "__main__":
    URL = 'https://api.github.com/user'
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATA = {'username': USERNAME, 'password': PASSWORD}
    RESULT = requests.get(URL, auth=HTTPBasicAuth(
        USERNAME, PASSWORD), timeout=5)
    RESULTJSON = RESULT.json()
    try:
        print(RESULTJSON.get('id'))
    except KeyError:
        print("None")
