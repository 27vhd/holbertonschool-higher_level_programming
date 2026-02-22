#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find the biggest integer of a list.

    Args:
        my_list (list): The list of integers to search.

    Returns:
        int: The biggest integer in the list, or None if the list is empty.
    """
    if not my_list:
        return None
    max_int = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > max_int:
            max_int = my_list[i]
    return max_int
