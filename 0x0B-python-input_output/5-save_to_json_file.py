#!/usr/bin/python3
"""input output task"""


import json


def save_to_json_file(my_obj, filename):
    """save json string to file"""
    with open(filename, "w") as new:
        json.dump(my_obj, new)
