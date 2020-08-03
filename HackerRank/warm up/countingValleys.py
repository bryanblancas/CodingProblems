#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    a = []
    is_valley = False

    for i in range(0, n):
        ch = s[i]

        if(len(a) == 0):
            if(ch == 'D'):
                is_valley = True
            a.append(ch)
        
        else:
            ch_a = a.pop()

            if(ch == 'D'):
                if(ch_a == 'D'):
                    a.append(ch_a)
                    a.append(ch)
            elif (ch == 'U'):
                if(ch_a == 'U'):
                    a.append(ch_a)
                    a.append(ch)

        if(len(a) == 0 and is_valley == True):
            valleys += 1
            is_valley = False
    
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
