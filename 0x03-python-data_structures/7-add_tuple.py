#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
        function that adds 2 tuples
    """
    if tuple_a == ():
        tuple_a = 0, 0
    if tuple_b == ():
        tuple_b = 0, 0
    if len(tuple_a) < 2:
        tuple_a = tuple_a[0], 0
    if len(tuple_b) < 2:
        tuple_b = tuple_b[0], 0
    tuple_item1 = tuple_a[0] + tuple_b[0]
    tuple_item2 = tuple_a[1] + tuple_b[1]
    new_tuple = tuple_item1, tuple_item2
    return new_tuple
