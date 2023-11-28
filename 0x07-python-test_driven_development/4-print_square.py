#!usr/bin/python3
"""print square function"""


def print_square(size):
    """ print square function
    args:
        size: the size of the square
    raise:
        type error if the size is not inriger
        value error if the size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
