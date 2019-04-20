#!/bin/python3

import math
import os
import random
import re
import sys

def count_a(s, m):
    n_a = 0

    for i in range(0, m):
        if(s[i] == 'a'):
            n_a += 1
            
    return n_a

# Complete the repeatedString function below.
def repeatedString(s, n):
    len_s = len(s)
    repeat = int(n/len_s)
    n_a = count_a(s, len_s)
    repeat *= n_a
    repeat += count_a(s, n%len_s)
    return repeat

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()
    s = "ab"
    #n = int(input())
    n = 759842

    result = repeatedString(s, n)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
