#!/usr/bin/python3
""" input output task"""


def write_file(filename="", text=""):
    """read file function"""
    with open(filename, "w") as new:
        return new.write(text)
