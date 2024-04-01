#!/usr/bin/env python3
"""Script that fetches https://intranet.hbtn.io/status"""
import urllib.request
URL = 'https://alx-intranet.hbtn.io/status'
if __name__ == "__main__":
    with urllib.request.urlopen(URL) as response:
        html = response.read()
        print('Body response:')
        print(f'\t- type: {type(html)}')
        print(f'\t- content: {html}')
        print(f"\t- utf8 content: {html.decode('utf-8')}")
