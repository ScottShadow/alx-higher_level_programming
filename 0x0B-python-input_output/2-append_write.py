#!/usr/bin/python3
"""File Appending Function Module"""


def append_write(filename="", text=""):
    """
    Appends the specified text to a file.

    Args:
        filename (str): The name of the file to which text will be appended.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
