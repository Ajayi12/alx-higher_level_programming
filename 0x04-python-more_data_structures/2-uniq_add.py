#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
        function that adds all unique integers in a list
    """
    new_list = list(set(my_list))
    sums = 0
    for x in new_list:
        sums += x
    return sums
