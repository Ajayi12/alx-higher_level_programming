#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
        function that deletes a key in a dictionary.
    """
    if key == "" or key not in a_dictionary:
        return a_dictionary
    else:
        del a_dictionary[key]
        return a_dictionary
