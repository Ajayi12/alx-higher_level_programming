#!/usr/bin/python3
def no_c(my_string):
    """
        function that removes all characters c and C from a string
    """
    new_string = []
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string.append(char)
    new_string = "".join(new_string)
    return new_string
