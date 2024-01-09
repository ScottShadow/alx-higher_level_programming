#!/usr/bin/python3
"""File Writing Function Module"""


def write_file(filename="", text=""):
    """
    Writes the specified text to a file.

    Args:
        filename (str): The name of the file to be written.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
