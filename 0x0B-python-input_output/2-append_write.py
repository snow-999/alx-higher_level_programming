#!/usr/bin/python3
""" input output task"""


def append_write(filename="", text=""):
    """read file function"""
    with open(filename, "a") as new:
        return new.write(text)
