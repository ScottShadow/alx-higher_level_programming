#!/usr/bin/python3
"""JSON Serialization Function Module"""

import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON-formatted string.

    Args:
        my_obj: The Python object to be serialized to JSON.

    Returns:
        str: A JSON-formatted string representing the input object.
    """
    return json.dumps(my_obj)
