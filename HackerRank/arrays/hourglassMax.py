#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
	addition = 0
	hourglass_max = -64

	for i in range(0,4):
		for j in range(0,4):
			addition = 0
			addition += arr[i][j]
			addition += arr[i][j+1]
			addition += arr[i][j+2]
			addition += arr[i+1][j+1]
			addition += arr[i+2][j]
			addition += arr[i+2][j+1]
			addition += arr[i+2][j+2]

			if(addition > hourglass_max):
				hourglass_max = addition
				#print("max in : "+str(i)+" , "+str(j))
    		
    
	return hourglass_max

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = [ [0,-4,-6,0,-7,-6],
			[-1,-2,-6,-8,-3,-1],
			[-8,-4,-2,-8,-8,-6],
			[-3,-1,-2,-5,-7,-4],
			[-3,-5,-3,-6,-6,-6],
			[-3,-6,0,-8,-6,-7],]

   #for _ in range(6):
    #    arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print (result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
