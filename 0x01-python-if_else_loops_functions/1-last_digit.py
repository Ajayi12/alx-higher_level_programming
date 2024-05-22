#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number1 = str(number)
length = len(number1)
temp = number1[length - 1]
if number1[0] == "-":
    temp = -(int(temp))
else:
    temp = int(temp)

if temp > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, temp))
elif temp < 6 and temp != 0:
    print("Last digit of {} is {} and is less than 6 and not 0"
            .format(number, temp))
else:
    print("Last digit of {} is {} and is 0".format(number, temp))
