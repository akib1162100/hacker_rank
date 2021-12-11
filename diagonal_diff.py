#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_diagonal = 0
    right_diagonal = 0
    length = len(arr)
    for i in range(length):
        left_diagonal += arr[i][i]
        right_diagonal += arr[i][(length-1) - i]
    return abs(left_diagonal - right_diagonal)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
