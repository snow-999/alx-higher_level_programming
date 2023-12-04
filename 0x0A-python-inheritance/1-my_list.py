#!/usr/bin/python3
"""function to print sorted list"""


class MyList(list):
    """class my list"""
    def print_sorted(self):
        """function return sotred list"""
        print(sorted(self))
