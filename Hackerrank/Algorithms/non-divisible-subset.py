#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    #making the rem dict
    rem={}
    for i in range(0,k):
        rem[i]=0
    #adding the s set values count in the rem dict
    for val in s:
        rem[val%k]=rem[val%k] + 1
    #getting the count by seeing which combination of rems make the sum divisible
    count=0
    #getting the multiples couples out of the way
    if rem[0]>0:
        count+=1
    #onto others
    for i in range (1,k//2+1):
        if k/i==2:
            count+=1
        else:
            num=max(rem[i],rem[k-i])
            count+=num
    return count
   
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()