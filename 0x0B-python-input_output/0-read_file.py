#!/usr/bin/python3
"""File Reading Function Module"""


def read_file(filename=""):
    """
    Reads and prints the contents of a text file.

    Args:
        filename (str): The name of the file to be read.

    Raises:
        FileNotFoundError: If the specified file is not found.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
