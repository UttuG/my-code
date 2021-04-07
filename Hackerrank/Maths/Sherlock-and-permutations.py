#!/bin/python3

import os
import sys

#
# Complete the divisors function below.
#
def divisors(n):
    i=0
    for x in range(1,int(n**0.5)+1):
        if n%x==0:
            if x%2==0:
                i+=1
            if (n/x)%2==0 and (x**2)!=n:
                i+=1
    return i        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()
