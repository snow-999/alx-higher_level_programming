#!/usr/bin/python3
"""input output task"""


import json


def load_from_json_file(filename):
    """creat an json file"""
    with open(filename, "w") as new:
        return json.load(new)
