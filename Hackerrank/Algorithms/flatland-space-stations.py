#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    maxint=0
    if len(c)<2:
        for i in range(0,n):
            y=abs(i-c[0])
            if y>maxint:
                maxint=y
        return maxint
    else:
        count=0
        for i in range(0,n):
            y=min(abs(i-c[0+count]),abs(i-c[1+count]))
            if y>maxint:
                maxint=y
            if abs(i-c[1+count])<abs(i-c[0+count]) and (len(c)-1)>=1+count+1:
                count+=1       
        return maxint
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()