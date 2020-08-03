#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):

    stack = []
    string = "YES"

    for ch in s:

        if(ch == '\n'):
            continue

        if(ch == '{' or ch == '[' or ch == '('):
            stack.append(ch)
        else:
            ch_stack = ''
            a = len(stack)

            if(a == 0):
                string = "NO"
                break
            ch = stack.pop()

            if(ch_stack == '{' and ch != '}'):
                string = "NO"
                break
            elif(ch_stack == '[' and ch != ']'):
                string = "NO"
                break
            elif(ch_stack == '(' and ch != ')'):
                string = "NO"
                break

    if(len(stack) != 0):
        string = "NO"

    return string

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    file = open("input_bracketBalanced.txt", 'r')
    t = int(file.readline())

    for t_itr in range(t):
        s = file.readline()
        #s = "[()][{}()][](){}([{}(())([[{}]])][])[]([][])(){}{{}{[](){}}}()[]({})[{}{{}([{}][])}]"
        result = isBalanced(s)
        print(result)
      #  fptr.write(result + '\n')

    #fptr.close()
