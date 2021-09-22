#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    c_dict={}
    for s in b:
        if s in c_dict:
            c_dict[s]+=1
        else:
            c_dict[s]=1
    #single colour scenario
    for i in c_dict:
        if c_dict[i]==1:
            if i!="_":
                return "NO"
    #no space scenario
    if "_" not in c_dict:
        for i,s in enumerate(b):
            if i==0:
                if b[1]!=s:
                    return "NO"
                else:
                    continue
            if i==len(b)-1:
                if b[i-1]!=s:
                    return "NO"
                else:
                    continue
            if b[i-1]!=s and b[i+1]!=s:
                return "NO"
    return "YES"          