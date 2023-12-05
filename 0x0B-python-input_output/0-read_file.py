#!/usr/bin/python3
""" input output task"""


def read_file(filename=""):
    """read file function"""
    with open(filename, encoding= "UTF8") as file:
        print(file.read())
