#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.

    Returns:
        The real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print(my_list[i], end="")
                count += 1
        except IndexError:
            break
    print()
    return count
