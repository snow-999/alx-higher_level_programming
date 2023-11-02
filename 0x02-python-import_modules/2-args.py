#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arc = len(sys.argv) -1
    if arc == 0:
        print("0 arguments.")
    elif arc == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:")
    for i in range(arc):
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
