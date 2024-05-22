#!/usr/bin/python3

for i in range(10):
    num2 = i + 1
    for n in range(num2, 10):
        if i == 8 and n == 9:
            print("{}{}".format(i, n))
        else:
            print("{}{}".format(i, n), end=", ")
