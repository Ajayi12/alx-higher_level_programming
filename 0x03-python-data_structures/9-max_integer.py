#!/usr/bin/python3
def max_integer(my_list=[]):
    """
        function that finds the biggest integer of a list.
    """
    n = 1
    i = 0
    temp = None
    length = len(my_list)
    if my_list == []:
        return None
    while i < 1:
        temp = my_list[i]
        while n < length:
            if temp < my_list[n]:
                temp = my_list[n]
            n += 1
        i += 1
    return temp
