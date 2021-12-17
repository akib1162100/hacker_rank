#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    a=sorted(a)
    b=sorted(b)
    count=0
    for i in range(a[len(a)-1],b[0]+1):
        flg_one=0
        flg_two=0
        for k in range(len(a)):
            if i%a[k]==0:
                flg_one+=1
        for j in range(len(b)):
            if b[j]%i==0:
                flg_two+=1
        if (flg_one==len(a)) and (flg_two==len(b)):
            count+=1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
    print(total)

    # fptr.write(str(total) + '\n')

    # fptr.close()
