#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    num = 0
    res = 0
    roman_numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for r in reversed(roman_string):
        num = roman_numbers[r]
        if res < num * 5:
            res += num
        else:
            res -= num
    return res
