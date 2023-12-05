#!/usr/bin/python3
""" input output task"""


def read_file(filename=""):
    """read file function"""
    with open(filename, "r") as file:
        print(file.read())
