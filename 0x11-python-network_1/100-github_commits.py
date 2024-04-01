#!/usr/bin/python3

"""
Print all commits by: `<sha>: <author name>` (one by line)
"""

import sys
import requests
if __name__ == "__main__":
    REPONAME = sys.argv[1]
    AUTHOR = sys.argv[2]
    URL = f"https://api.github.com/repos/{AUTHOR}/{REPONAME}/commits"

    RESULTS = requests.get(URL, timeout=5)
    RESULTS_JSON = RESULTS.json()
    size = len(RESULTS_JSON)

    for i in range(0, 10):
        if i >= size:
            break
        sha = RESULTS_JSON[i].get('sha')
        name = RESULTS_JSON[i].get('commit').get('author').get('name')
        print(f'{sha}: {name}')
