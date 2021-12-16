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
    max_num = 0
    min_val = 99999999999999
    for i in range(0,len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                if abs(arr[i]*arr[j]*arr[k]) > max_num:
                    max_num = abs(arr[i]*arr[j]*arr[k])
                if abs(arr[i]*arr[j]*arr[k]) < min_val:
                    min_val = abs(arr[i]*arr[j]*arr[k])
    
    return str(min_val) + " " + str(max_num)
    


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