#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely and handles exceptions.

    Args:
        fct: The function to execute.
        args: Arguments for the function.

    Returns:
        The result of the function, or None if an exception occurs.
    """
    try:
        # Funksiyanı gələn arqumentlərlə çağırırıq
        result = fct(*args)
        return result
    except Exception as e:
        # Xətanı stderr-ə çap edirik
        print("Exception: {}".format(e), file=sys.stderr)
        return None
