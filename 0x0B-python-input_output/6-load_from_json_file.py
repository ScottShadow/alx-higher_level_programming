#!/usr/bin/python3
"""JSON File Loading Function Module"""

import json


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON-formatted file.

    Args:
        filename (str): The name of the file from which the
        object will be loaded.

    Returns:
        Any: The Python object representing the loaded JSON.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            return json.loads(line)
