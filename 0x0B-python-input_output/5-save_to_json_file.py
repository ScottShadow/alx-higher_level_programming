#!/usr/bin/python3
"""JSON File Saving Function Module"""

import json


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a JSON-formatted file.

    Args:
        my_obj: The Python object to be saved.
        filename (str): The name of the file to which the object will be saved.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
