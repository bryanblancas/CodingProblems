#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n,k):
    if(len(n) == 1):
        return n
    
    p = 0
    for x in n:
        p += int(x)
    return superDigit(str(p*k), 1)

if __name__ == '__main__':
    file = open("input.txt", "r")
    nk = ""
    nk = file.read().split()
    
    n = nk[0]
    k = int(nk[1])

    result = superDigit(n,k)

    print str(result)

    file.close()