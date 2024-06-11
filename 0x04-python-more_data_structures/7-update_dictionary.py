#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
        function that replaces or adds key/value in a dictionary.
    """
    for i, element in a_dictionary.items():
        if i == key:
            a_dictionary[i] = value
            return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
