#!/usr/bin/python3

def multiple_returns(sentence):
    """
        function that returns a tuple with
        the length of a string and its first character
    """
    length = len(sentence)
    if length == 0:
        return length, None
    return length, sentence[0]
