#!/usr/bin/python3

def element_at(my_list, idx):
    """
        function that retrives an element from a list
    """
    length = len(my_list)
    if idx < 0:
        return None
    elif idx > length:
        return None
    else:
        return my_list[idx]
