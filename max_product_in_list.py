#!/usr/bin/env python3
'''
Given a list of elements 'mylist' find the maximum product of two numbers found in the list
eg. mylist = [4, 2, 1, 3, 5]
    max_product is 5 x 4 = 20
'''
import random

def max_product_list(mylist) -> int:
    product = 0
    if mylist is None or len(mylist) == 0:
        return product
    elif len(mylist) == 1:
        return mylist[0]
    else:
        a, b = sorted(mylist, reverse=True)[:2]
        return a * b


def max_product(*args) -> int:
    if len(args) == 1 and (type(args[0]) is list):
        return max_product_list(args[0])
    else:
        return max_product_list([arg for arg in args])


if __name__ == "__main__":
    assert max_product() == 0
    assert max_product(99) == 99
    assert max_product(4, 2, 3, 1) == 12
    assert max_product([45]) == 45
    assert max_product([4, 2, 1, 3, 5]) == 20
    assert max_product([29, 23, 58, 41, 57, 36, 4, 15, 47, 26, 65, 66, 90, 21, 56, 17, 63, 93, 79, 42, 55, 96, 35, 69, 6, 12, 88, 59, 81, 67, 32, 5, 70, 8, 76, 40, 11, 39, 49, 16, 73, 83, 43, 46, 71, 27, 72, 74, 48, 30, 18, 89, 9, 24, 77, 2, 13, 10, 98, 84, 62, 3, 87, 60, 82, 85, 91, 45, 94, 97, 34, 75, 25, 37, 51, 7, 54, 53, 80, 99, 92, 28, 44, 50, 38, 31, 22, 61, 68, 14, 78, 52, 33, 20, 95, 19, 64, 1, 86]) == 9702
    # test with shuffled million numbers
    rand_million = list(range(1, 1_000_000))
    random.shuffle(rand_million)
    assert max_product(rand_million) == 999997000002