#!/usr/bin/python3
""" input output task"""


def read_file(filename=""):
    """read file function"""
    with open(filename, encoding="uft-8") as new_file:
        print(new_file.read(), end="")
