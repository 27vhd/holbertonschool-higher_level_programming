#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list.

    Args:
        my_list (list): The list to delete the item from.
        idx (int): The index of the item to delete.

    Returns:
        The modified list or None if the index is out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    del my_list[idx]
    return my_list
