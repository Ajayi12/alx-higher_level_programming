#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
        function that returns a set of common elements in two sets.
    """
    result = list(filter(lambda x: x in set_1, set_2))
    return result
