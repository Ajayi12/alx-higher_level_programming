#!/usr/bin/python3

def roman_to_int(roman_string):
    """
        function that converts a Roman numeral to an integer.
    """
    new_list = []
    sums = 0
    n = 0
    if type(roman_string) != str or roman_string == None:
        return 0
    roman_keys = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for char in roman_string:
        temp = roman_keys[char]
        new_list.append(temp)
    for i in range(len(new_list)):
        temps = new_list[i - n]
        n = 1
        if temps < new_list[i]:
            num = temps * 2
            sums = sums + new_list[i] - num
        else:
            sums += new_list[i]
    return sums
