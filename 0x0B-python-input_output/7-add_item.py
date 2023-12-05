#!/usr/bin/python3
"""input output task"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


argTsave = list(sys.argv[1:])

try:
    deta = load_from_json_file("add_item.json")
except Exception:
    deta = []

deta.extend(argTsave)
save_to_json_file(deta, "add_item.json")
