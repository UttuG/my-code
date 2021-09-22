#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    rows=len(A)
    cols=len(A[0])
    cost=2*rows*cols#top and bottom counted
    for i,r in enumerate(A):
        for c in range(cols):
            #north
            if i+1<=rows-1:
                cost+=max(r[c]-A[i+1][c],0)
            else:
                cost+=r[c]
            #south
            if i-1>=0:
                cost+=max(r[c]-A[i-1][c],0)
            else:
                cost+=r[c]
            #east
            if c+1<=cols-1:
                cost+=max(r[c]-A[i][c+1],0)
            else:
                cost+=r[c]
            #west
            if c-1>=0:
                cost+=max(r[c]-A[i][c-1],0)
            else:
                cost+=r[c]
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
