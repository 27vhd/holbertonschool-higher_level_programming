#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """Returns a list with all values multiplied by a number.

    Args:
        my_list (list): A list of integers.
        number (int): The number to multiply the list values by.

    Returns:
        A new list with all values multiplied by the number.
    """
    return list(map(lambda x: x * number, my_list))
