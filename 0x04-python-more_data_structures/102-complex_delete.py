#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    char = str(value)
    new = []
    for k, v in a_dictionary.items():
        if v == char:
            new.append(k)
    for element in new:
        del a_dictionary[element]
    return a_dictionary
