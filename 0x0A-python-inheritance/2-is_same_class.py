#!/usr/bin/python3
"""function to find the type"""


def is_same_class(obj, a_class):
    """find if inhartance"""
    if type(obj) == a_class:
        return True
    else:
        return False
