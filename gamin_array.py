#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    # Write your code here
    i = 0
    while True:
        length = len(arr)
        if length == 0:
            # i += 1    
            break
        max_num = max(arr)
        get_index = arr.index(max_num)

        if get_index == length - 1:
             del arr[get_index]
        else:
            del arr[get_index:length-1]
        i += 1
    
    # print(i)
    if i % 2 == 0:
        return "BOB"
    else:
        return "ANDY"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)
        print(result)
    #     fptr.write(result + '\n')

    # fptr.close()