#!/usr/bin/python3

def islower(c):
    arr = "abcdefghijklmnopqrstuvwxyz"
    length = len(arr)
    for i in range(length):
        if c == arr[i]:
            return True
    else:
        return False
