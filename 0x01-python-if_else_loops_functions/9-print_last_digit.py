#!/usr/bin/python3

def print_last_digit(number):
    number = str(number)
    length = len(number)
    temp = number[length - 1]
    temp = int(temp)
    print(temp, end="")
    return (temp)
