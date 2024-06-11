#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
        function that replaces all occurrences of an element by another in a new list
    """
    result = list(map(lambda x: x if x != search else replace, my_list))
    return result
