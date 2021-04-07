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
#neo now knows regex so short code now :)
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
str1="".join(matrix[x][y] for y in range(0,m) for x in range(0,n))
result=re.sub(r"([A-Za-z0-9])[^A-Za-z0-9]+([?=A-Za-z0-9])",r"\1 \2",str1)
print(result)       
