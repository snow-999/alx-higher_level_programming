#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listD = []
    for i in my_list:
        if i % 2 == 0:
            listD.append(True)
        else:
            listD.append(False)
    return listD
