#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxkey = None
    maxvalue = 0
    for k, v in a_dictionary.items():
        if v > maxvalue:
            maxkey = k
            maxvalue = v
    return maxkey
