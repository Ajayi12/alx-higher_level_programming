#!/usr/bin/python3

def uppercase(str):
    for char in str:
        temp = ord(char)
        if temp >= 97 and temp <= 122:
            temp -= 32
            temp = chr(temp)
        else:
            temp = chr(temp)
        print(f"{temp}", end="")
    print()
