#!/bin/python3

import math
import os
import random
import re
import sys
import string
#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    arr=[i for i in range(1,n+1)]
    flag_l=[0 for i in range(n)]
    if n%2!=0:
        if k==0:
            return arr
        else:
            return [-1]
    else:
        if k==0:
            return arr
        if n%(k*2)==0:#for pattern to repeat, it needs multiples of its width
            for i in range(n):
                if flag_l[i]==0:
                    arr[i],arr[k+i]=arr[k+i],arr[i]
                    flag_l[i],flag_l[k+i]=1,1
            return arr
        else:
             return [-1]          
    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
