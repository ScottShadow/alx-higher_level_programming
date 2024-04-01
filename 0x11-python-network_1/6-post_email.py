#!/usr/bin/python3
"""
takes in a URL and an email address, sends a POST request to the passed URL 
with the email as a parameter, and finally displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    URL = sys.argv[1]
    EMAIL = sys.argv[2]
    DATA = {'email': EMAIL}
    RESULT = requests.post(URL, data=DATA, timeout=5)
    print(RESULT.text)
