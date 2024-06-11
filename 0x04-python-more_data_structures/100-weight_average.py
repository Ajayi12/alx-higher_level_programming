#!/usr/bin/python3

def weight_average(my_list=[]):
    """
        function that returns the weighted average
    """
    sums = 0
    sums_2 = 0
    if my_list == []:
        return 0
    score = list(map(lambda x: x[0] * x[1], my_list))
    new_weigth = list(map(lambda x: x[1], my_list))
    for num in score:
        sums += num
    for i in new_weigth:
        sums_2 += i
    return sums / sums_2
