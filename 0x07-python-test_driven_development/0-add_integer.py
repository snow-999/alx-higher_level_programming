#!/usr/bin/python3
"""add two integers"""


def add_integer(a, b=98):
    """
    add two intigers

    args:
        a: first number
        b: second number
    raise:
        typer error if it's not number
    return:
        the sum of two digits
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return a+b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
