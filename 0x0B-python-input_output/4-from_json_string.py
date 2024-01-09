#!/usr/bin/python3
"""JSON Deserialization Function Module"""

import json


def from_json_string(my_str):
    """
    Converts a JSON-formatted string to a Python object.

    Args:
        my_str (str): The JSON-formatted string to be deserialized.

    Returns:
        Any: The Python object representing the deserialized JSON.
    """
    return json.loads(my_str)
