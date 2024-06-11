#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
        function that prints a dictionary by ordered keys.
    """
    my_dict = sorted(a_dictionary.keys())
    for key in my_dict:
        print("{}: {}".format(key, a_dictionary[key]))
