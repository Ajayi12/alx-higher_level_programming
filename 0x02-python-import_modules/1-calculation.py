#!/usr/bin/python3
import calculator_1 as cal
if __name__ == "__main__":
    a = 10
    b = 5
    add = cal.add(a, b)
    print("{} + {} = {}".format(a, b, add))

    sub = cal.sub(a, b)
    print("{} - {} = {}".format(a, b, add))

    mul = cal.mul(a, b)
    print("{} * {} = {}".format(a, b, mul))

    div = cal.div(a, b)
    print("{} / {} = {}".format(a, b, div))
