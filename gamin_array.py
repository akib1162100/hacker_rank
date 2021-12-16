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
    # Write your code here
    Counter = 0
    arr_max = 0
    for i in range(len(arr)):
        if arr[i] > arr_max:
            arr_max = arr[i]
            Counter +=1
   
    if Counter % 2 == 0:
        return "ANDY"
    else:
        return "BOB"




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