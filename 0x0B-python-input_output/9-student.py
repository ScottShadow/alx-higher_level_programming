#!/usr/bin/python3
"""Student Class Module"""


class Student:
    """
    Represents a student with first name, last name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Constructor method for creating a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts the Student object to a dictionary.

        Returns:
            dict: A dictionary representing the attributes
            of the Student object.
        """
        return vars(self)
