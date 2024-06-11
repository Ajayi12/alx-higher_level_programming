#!/usr/bin/python3

def best_score(a_dictionary):
    """
        function that returns a key with the biggest integer value
    """
    if a_dictionary is None or a_dictionary is {}:
        return None
    for k, v in a_dictionary.items():
        x_value = v
        x_key = k
    for key, val in a_dictionary.items():
        if x_value < val:
            x_value = val
            x_key = key
    return x_key
