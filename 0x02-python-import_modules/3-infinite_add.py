#!/usr/bin/python3

import sys
if __name__ == "__main__":
    length = len(sys.argv)
    i = 1
    sums = 0
    if length == 1 or length == 0:
        print("0")
    else:
        while i < length:
            num = int(sys.argv[i])
            sums += num
            i += 1
        print("{}".format(sums))
