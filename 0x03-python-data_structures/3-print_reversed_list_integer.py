#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
        function that prints all integers of a list, in reverse order.
    """
    length = len(my_list) - 1
    for i in range(length + 1):
        temp = my_list[length - i]
        print("{:d}".format(temp))
