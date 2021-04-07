#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
  #checking for first occurence of uncommon element
    for i in range(0,(min(len(s),len(t)))):
        if s[i]!=t[i]:
            i-=1
            break
  #checking no of steps required
    eff_k=len(s)-(i+1)+len(t)-(i+1)
    ex_k=k-eff_k
  #conditions for yes/no
    if ex_k==0:
        return "Yes"
    if ex_k<0:
        return "No"
    if ex_k>0:
        if ex_k%2==0:
            return "Yes"
        else:
            if ex_k<=i+1:
                return "No"
            else:
                if ex_k>=2*(i+1):
                    return "Yes"
                else:
                    return "No"
  
  
        
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()