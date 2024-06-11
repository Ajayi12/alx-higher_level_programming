#!/usr/bin/python3

def number_keys(a_dictionary):
    """
        function that returns the number of keys in a dictionary
    """
    sums = 0
    for i, v in enumerate(a_dictionary):
        sums += 1
    return sums
