#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    s = s.split(" ")
    newString = ""
    newList = []
    
    for _ in s:
        newString = ""
        for x,y in enumerate(_):
            
            if x == 0:
                newString = y.upper()
            else:
                newString += y
        
        newList.append(newString)
    return ' '.join(newList)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
