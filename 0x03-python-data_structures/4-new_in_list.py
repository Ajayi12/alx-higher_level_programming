#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
        function that replaces an element in a list
        at a specific position without modifying the original list
    """
    length = len(my_list)
    if idx < 0:
        return my_list.copy()
    if idx > length - 1:
        return my_list.copy()
    copied_list = my_list.copy()
    copied_list[idx] = element
    return copied_list
