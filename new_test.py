#!/bin/python3

import math
import os
import random
import re
import sys
from typing import TextIO


def consumer():
    while True:
        x = yield
        print(x)

def producer(n):
    for _ in range(n):
        x = int(input())
        yield x


# Complete the 'rooter', 'squarer', and 'accumulator' function below.

def rooter():
    # Write your code here
    x = yield
    while True:
        root = math.sqrt(x)
        yield (math.floor(root))
    

def squarer():
    # Write your code here
    x = yield
    while True:
        square = x*x
        yield square


def accumulator():
    total = 0
    # Write your code here
    x = yield
    while True:
        x = x + total
        total = x
        yield total
        


def pipeline(prod, workers, cons):

    for num in prod:
        for i, w in enumerate(workers):
            num = w.send(num)
        cons.send(num)
    for worker in workers:
        worker.close()
    cons.close()

if __name__ == '__main__':
    order = input().strip()
    
    n = int(input())
    prod = producer(n)

   
    cons = consumer()
    next(cons)

    root = rooter()
    next(root)
    square = squarer()
    next(square)

    accumulate = accumulator()
    next(accumulate)


    pipeline(prod, eval(order), cons)
