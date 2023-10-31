#!/usr/bin/python3
for i in range(10):
    for x in range(i, 10):
        if i < x and i + x != 17:
            print("{:d}{:d}".format(i, x),end=', ')
        if i + x == 17:
            print("{:d}{:d}".format(i, x))
