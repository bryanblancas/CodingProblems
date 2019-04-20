#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    i = 0
    print(arr)
    while i < len(arr):
        #print("iteracion: "+str(i))
        if(arr[i] > (i+1)):
            #print("Swap: arra["+str(arr[i]-1)+"] and arr["+str(i)+"]")
            aux = arr[arr[i]-1]
            arr[arr[i]-1] = arr[i]
            arr[i] = aux
            swaps += 1
        else:
            i += 1
    print(arr)
    return swaps

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())

    #arr = list(map(int, input().rstrip().split()))

    arr = [6,5,4,3,2,1]
    res = minimumSwaps(arr)
    print(res)
    #fptr.write(str(res) + '\n')

    #fptr.close()
