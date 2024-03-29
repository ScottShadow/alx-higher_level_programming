#!/usr/bin/python
"""find_peak Module"""


def find_peak(list_of_integers):
    """
    Find the peak element in a list of integers using binary search.

    Args:
        list_of_integers (List[int]): A list of integers to search
        for the peak.

    Returns:
        int: The peak element in the list.
    """
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
