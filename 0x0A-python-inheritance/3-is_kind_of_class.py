#!/usr/bin/python3
"""function to find the same kind"""


def is_kind_of_class(obj, a_class):
    """find if inhartance"""
    if type(obj) == a_class or isinstance(obj, a_class):
        return True
    else:
        return False
