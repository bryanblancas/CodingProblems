#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):

    len_a = len(a)
    swaps = 0

    for i in range(len_a):
        for j in range(len_a-1):
            if(a[j] > a[j+1]):
                aux = a[j]
                a[j] = a[j+1] 
                a[j+1] = aux
                swaps += 1

    print("Array is sorted in "+str(swaps)+" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
