#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters c and C from a string.

    Args:
        my_string (str): The string to remove characters from.

    Returns:
        str: The new string with characters removed.
    """
    new_string = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_string += my_string[i]
    return new_string
