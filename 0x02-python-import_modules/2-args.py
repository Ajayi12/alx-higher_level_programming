#!/usr/bin/python3

import sys

length = len(sys.argv)
i = 1
if length == 1 or length == 0:
    print("0 arguments.")
else:
    print(f"{length - 1} arguments:")
    while i < length:
        print(f"{i}: {sys.argv[i]}")
        i += 1
