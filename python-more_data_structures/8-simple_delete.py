#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to delete from.
        key: The key to delete.

    Returns:
        The dictionary after deletion of the key.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
