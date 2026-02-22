#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Add 2 tuples.

    Args:
        tuple_a (tuple): The first tuple to add.
        tuple_b (tuple): The second tuple to add.

    Returns:
        A tuple with 2 integers: the sum of the first and second
        integers of each argument.
    """
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a1 + b1, a2 + b2)
