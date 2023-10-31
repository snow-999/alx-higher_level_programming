#!/usr/bin/python3
def islower(c):
    if c >= chr(97) and c <= chr(122):
        return True
    else:
        return False

def uppercase(str):
    for c in str:
        print("{:c}".format(ord(c) if islower(c) is False
                            else ord(c) - 32), end="")
    print('')
