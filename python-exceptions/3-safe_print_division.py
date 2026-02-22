#!/usr/bin/python3

def safe_print_division(a, b):
    """Prints the result of the division of a by b.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The value of the division, otherwise None if
        the division cannot be performed.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
