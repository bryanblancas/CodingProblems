#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    i = 0
    jumps = 0
    len_c = len(c)

    if(c[len_c-1] == 1):
        print("Can not reach final")
        return jumps

    while(i < len_c-1):

        if(i+2 < len_c):
            if(c[i+2] == 0):
                i += 2
                jumps += 1
                continue

        if(i+1 < len_c):
            if(c[i+1] == 0):
                i += 1
                jumps += 1
                continue

    return jumps

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())

    #c = list(map(int, input().rstrip().split()))
    c = [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0]

    result = jumpingOnClouds(c)
    print (result)
    print(1000000000000*100)
    #fptr.write(str(result) + '\n')

    #fptr.close()
