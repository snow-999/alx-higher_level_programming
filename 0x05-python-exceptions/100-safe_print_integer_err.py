#!/usr/bin/python3
import sys


def safe_print_integer(value):
    is_int = True
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        is_int = False
