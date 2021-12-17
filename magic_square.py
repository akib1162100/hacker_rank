#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    sum_of_diagonal = sum(s[i][i] for i in range(len(s)))
    sum_of_other_diagonal = sum(s[i][len(s)-i-1] for i in range(len(s)))
    sum_of_middle_row = sum(s[i][len(s)//2] for i in range(len(s)))
    sum_of_middle_column = sum(s[len(s)//2][i] for i in range(len(s)))
    magic_number = 3*s[len(s)//2][len(s)//2]
    return abs(sum_of_diagonal - magic_number) + abs(sum_of_other_diagonal - magic_number) + abs(sum_of_middle_row - magic_number) + abs(sum_of_middle_column - magic_number)



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)

