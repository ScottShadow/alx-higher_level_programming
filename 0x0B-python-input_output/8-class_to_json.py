#!/usr/bin/python3
"""JSON Serialization and Deserialization Functions Module"""

import json
myclassmodule = __import__('8-my_class')
MyClass = getattr(myclassmodule, 'MyClass')


def myclass_serializer(obj):
    """
    Custom JSON serializer function for MyClass objects.

    Args:
        obj (MyClass): The object to be serialized.

    Returns:
        dict: A dictionary representing the serialized object.
    """
    return {'name': obj.name, 'number': obj.number}


def class_to_json(obj):
    """
    Custom JSON serialization function for MyClass objects.

    Args:
        obj: The object to be serialized.

    Returns:
        dict: A dictionary representing the serialized object.
    """
    if isinstance(obj, MyClass):
        return myclass_serializer(obj)
