#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
        function that finds all multiples of 2 in a list.
    """
    new_list = []
    length = len(my_list)
    for num in range(length):
        if my_list[num] % 2 == 0:
            new_list.append(1)
        else:
            new_list.append(0)
    return new_list
