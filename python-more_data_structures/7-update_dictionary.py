#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key: The key to replace or add.
        value: The value associated with the key.

    Returns:
        The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
