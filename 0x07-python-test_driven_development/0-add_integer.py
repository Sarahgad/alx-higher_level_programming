#!/usr/bin/python3
"""   a function that adds 2 integers
"""


def add_integer(a, b=98):

    """Add two integers
    Args:
    a (int) is the first element
    b (int) is the second element default by 98
    Returns:
             int: the sum of 'a' amd 'b'
    Raises:
    TypeError a  or b must be an integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)
