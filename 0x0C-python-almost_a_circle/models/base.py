#!/usr/bin/python3
"""
Module for Base Class and Related Functions

This module defines a Base class and provides utility functions for
handling JSON data.

Classes:
    Base: A simple base class with id attribute.

Functions:
    to_json_string(list_dictionaries): Convert a list of dictionaries
    to a JSON-formatted string.
    save_to_file(list_objs): Save a list of objects to a JSON file.
    from_json_string(json_string): Convert a JSON-formatted string to a
      list of dictionaries.
    create(cls, **dictionary): Create a new object instance and initialize
      its attributes from a dictionary.
    load_from_file(cls): Load objects from a JSON file and return a list
      of instances.

"""
import json


class Base:
    """
    Base Class

    Attributes:
        __nb_objects (int): A class attribute to keep track of the number of
        instances created.
        id (int): An instance attribute representing the identifier of
        an object.

    Methods:
        __init__(self, id=None): Constructor method to initialize the
        Base object.
        to_json_string(list_dictionaries): Static method to convert a
        list of dictionaries to a JSON-formatted string.
        save_to_file(cls, list_objs): Class method to save a list of
        objects to a JSON file.
        from_json_string(json_string): Static method to convert a
        JSON-formatted string to a list of dictionaries.
        create(cls, **dictionary): Class method to create a new object
          instance and initialize its attributes from a dictionary.
        load_from_file(cls): Class method to load objects from a JSON
        file and return a list of instances.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor Method

        Args:
            id (int): Optional parameter to set the identifier of
            the object.
                      If not provided, automatically increments the
                      identifier based on the number of instances.

        Returns:
            None
        """
        if not isinstance(id, type(None)):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): A list of dictionaries
            representing objects.

        Returns:
            str: A JSON-formatted string.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): A list of object instances.

        Returns:
            None
        """
        filename = f"{cls.__name__}.json"
        listdict = []
        for obj in list_objs:
            listdict.append(obj.to_dictionary())
        with open(filename, 'w+', encoding='utf-8') as f:
            f.write(cls.to_json_string(listdict))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON-formatted string to a list of dictionaries.

        Args:
            json_string (str): A JSON-formatted string.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new object instance and initialize its attributes
        from a dictionary.

        Args:
            **dictionary: Keyword arguments representing attribute-value pairs.

        Returns:
            cls: A new instance of the class with attributes initialized.
        """
        newobj = cls(1, 1)

        newobj.update(**dictionary)

        return newobj

    @classmethod
    def load_from_file(cls):
        """
        Load objects from a JSON file and return a list of instances.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        filename = f"{cls.__name__}.json"
        listdict = {}
        with open(filename, 'r+', encoding='utf-8') as f:
            listdict = f.read()
        newdict = cls.from_json_string(listdict)
        newlistobj = []
        for obj in newdict:
            newobj = cls.create(**obj)
            newlistobj.append(newobj)
        return newlistobj
