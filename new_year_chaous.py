#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Counter

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def gamingArray(arr):
    counter = 0
    # sort_array = sorted(arr)
    for i in range(len(arr)):
        if arr[i] != i+1:
            if arr[i-1] == i+1:
                counter += 1
                arr[i-1],arr[i] = arr[i],arr[i-1]
            elif arr[i-2] == i+1:
                counter += 2
                arr[i-2],arr[i-1] = arr[i-1],arr[i-2]
                arr[i-1],arr[i] = arr[i],arr[i-1]
            else:
                return "Too chaotic"
    return counter
# def gamingArray(arr):
#     # Write your code here
#     Counter = 0
#     arr_max = 0
#     sort_array = sorted(arr)
#     for i in range(len(arr)):
#         if sort_array.index(arr[i])-i > 2:
#             return ("Too chaotic")
#         if arr[i] > arr_max:
#             arr_max = arr[i]
#             Counter +=1
   
#     return (len(arr)-Counter)




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