#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    adds = add(a, b)
    print("{} + {} = {}".format(a, b, adds))

    subs = sub(a, b)
    print("{} - {} = {}".format(a, b, subs))

    muls = mul(a, b)
    print("{} * {} = {}".format(a, b, muls))

    divs = div(a, b)
    print("{} / {} = {}".format(a, b, divs))
