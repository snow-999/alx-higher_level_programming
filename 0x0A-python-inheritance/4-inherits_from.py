#!/usr/bin/python3
"""find the inhert class"""


def inherits_from(obj, a_class):
    """find if inhartance"""
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    else:
        return False
