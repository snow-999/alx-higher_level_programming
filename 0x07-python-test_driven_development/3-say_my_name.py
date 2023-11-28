#!/usr/bin/python3
"""print name"""


def say_my_name(first_name, last_name=""):
    """ print name function
        args:
            first_name: is the first name
            last_name: is the last name
        raise:
            type error if the first or last is not a str
        return:
            none
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
