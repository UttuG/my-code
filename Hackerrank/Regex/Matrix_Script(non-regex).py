#!/bin/python3

import math
import os
import random
import re
import sys
import string




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])
#neo still doesn't know regex,so he will be using while statements :)
matrix = []
sentence=[]
result=[]
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
#matrix to list
sentence=[matrix[x][y] for y in range(0,m) for x in range(0,n)]
#finding first occurence of alnum from right
y=sentence[(n*m)-1]
z=0
for i in range(0,n*m):
    while not y.isalnum(): 
        y=sentence[(n*m)-1-i]
        z+=1
        break
#finding first occurence of alnum from left
y=sentence[0]
q=0
for i in range(0,n*m):
    while not y.isalnum(): 
        y=sentence[i]
        q+=1
        break
#preparing the result sentence
while q!=z:
    for p in range(0,q):
        result.append(sentence[p])
    for p in range(q,(n*m)-z):
        while sentence[p].isalnum():
            result.append(sentence[p])
            break
        while not sentence[p].isalnum():
            result.append(" ")
            break
    for p in range((n*m)-z,n*m):
        result.append(sentence[p])
    break
while q==z:
    while q==0:
        for p in range(0,n*m):
            while sentence[p].isalnum():
                result.append(sentence[p])
                break
            while not sentence[p].isalnum():
                result.append(" ")
                break
        break
    while q!=0:
        for p in range(0,n*m):
            result.append(sentence[p])
        break
    break
#printing the result sentence
for t in result:
    print(t,end="")
        