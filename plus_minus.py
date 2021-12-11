#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    plus_counter = 0
    minus_counter = 0
    zero_counter = 0
    length = len(arr)
    for i in arr:
        if i > 0:
            plus_counter += 1
        elif i < 0:
            minus_counter += 1
        else:
            zero_counter += 1
    print("{:.6f}".format(plus_counter/length))
    print("{:.6f}".format(minus_counter/length))
    print("{:.6f}".format(zero_counter/length))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
