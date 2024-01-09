#!/usr/bin/python3
"""JSON File Manipulation Script"""

import json
import sys

# Importing functions from external modules
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

""" Extend the existing data with command-line arguments"""
data.extend(sys.argv[1:])

save_to_json_file(data, filename)
