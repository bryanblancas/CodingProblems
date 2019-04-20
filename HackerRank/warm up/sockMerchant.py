#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    a = {}

    for i in range(0, n):
        
        if(ar[i] in a.keys()):
            a[ar[i]] += 1
            if(a[ar[i]] == 2):
                pairs += 1
                a[ar[i]] = 0
        else:
            a[ar[i]] = 1

    print (a)
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
