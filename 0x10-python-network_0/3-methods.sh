#!/bin/bash
# takes in a URL and displays all HTTP methods on a server
curl -s -I -X OPTIONS "$1" | grep -i '^Allow:' | sed 's/Allow: //i'
