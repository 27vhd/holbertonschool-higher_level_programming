#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position without
    modifying the original list.

    Args:
        my_list (list): The list to replace the element in.
        idx (int): The index of the element to replace.
        element: The new element to replace the old one with.

    Returns:
        A new list with the modified element or the original list if
        the index is out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
