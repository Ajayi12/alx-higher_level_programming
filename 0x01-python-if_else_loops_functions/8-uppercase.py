#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if char.isalpha():
            temp = ord(char)
            if temp > 91:
                temp -= 32
                temp = chr(temp)
                print(f"{temp}", end="")
            else:
                temp = chr(temp)
                print(f"{temp}", end="")
        else:
            print(f"{char}", end="")
    print()
