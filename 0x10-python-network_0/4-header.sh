#!/bin/bash
#sends a GET request with specific Header content and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
