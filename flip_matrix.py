#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    inter= len(matrix)//2
    length = len(matrix)
    sum = 0
    for i in range(inter):
        for j in range(inter):
            sum += max(max(matrix[i][j],matrix[i][length-1-j]),max(matrix[length-1-i][j],matrix[length-1-i][length-1-j]))
    return sum


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)
        print(result)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
