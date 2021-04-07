#!/bin/python3

import os
import sys

#
# Complete the primeCount function below.
#
def primeCount(n):
   list1=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,57,59,61,67,71]
   x=1
   if n==1:
       return 0
   for i in list1:
       x*=i
       if x > n:
           return list1.index(i)
       if x==n:
           return list1.index(i) + 1
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()