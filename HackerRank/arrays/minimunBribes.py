#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(Q):
    len_q = len(q)
    bribes_total = 0
    
    for index,value in enumerate(q):
        if((value-1) - index > 2):
            print("Too chaotic")
            return
                
    for i in range(0, len_q):

        #print(str(q[i]-3)+":"+str(i))
        for j in range(max(q[i]-3,0),i):
            
            if(q[i] < q[j]):
                #print("q["+str(i)+"] = "+str(q[i])+" < "+"q["+str(j)+"] = "+str(q[j]))
                bribes_total += 1
  
    print(bribes_total)
    
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
