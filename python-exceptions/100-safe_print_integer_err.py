#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer and returns True, otherwise prints to stderr.

    Args:
        value: The value to print (any type).

    Returns:
        True if value is an integer and printed correctly, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        # Xəta mesajını sys.stderr vasitəsilə çap edirik
        print("Exception: {}".format(e), file=sys.stderr)
        return False
