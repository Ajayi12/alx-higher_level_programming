#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
        print list of integers
    """
    for i in range(len(my_list)):
        temp = my_list[i]
        print("{:d}".format(temp))
