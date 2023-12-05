#!/usr/bin/python3
""" input output task"""


def read_file(filename=""):
    """read file function"""
    with open(filename, "r") as new:
        print(new.read(), end="")
