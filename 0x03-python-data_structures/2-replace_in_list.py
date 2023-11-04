#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if not my_list:
        return None
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    my_list[idx] = element
    return my_list
