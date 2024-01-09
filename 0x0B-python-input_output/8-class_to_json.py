#!/usr/bin/python3
"""JSON Serialization and Deserialization Functions Module"""


def class_to_json(obj):
    """
    Custom JSON serialization function for MyClass objects.

    Args:
        obj: The object to be serialized.

    Returns:
        dict: A dictionary representing the serialized object.
    """
    if hasattr(obj, '__dict__'):
        return vars(obj)
