#!/usr/bin/python3

import sys
if __name__ == "__main__":
    length = len(sys.argv)
    i = 1
    if length == 1 or length == 0:
        print("0 arguments.")
    elif length == 2:
        print(f"{length - 1} argument:")
        while i < length:
            print(f"{i}: {sys.argv[i]}")
            i += 1
    else:
        print(f"{length - 1} arguments:")
        while i < length:
            print(f"{i}: {sys.argv[i]}")
            i += 1
