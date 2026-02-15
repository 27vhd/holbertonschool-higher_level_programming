#!/usr/bin/python3

def multiple_returns(sentence):
    """Return a tuple with the length of a string and its first character.

    If the sentence is empty, the first character should be equal to None.

    Args:
        sentence (str): The string to evaluate.

    Returns:
        tuple: A tuple containing the length of the string
        and its first character.
    """
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
