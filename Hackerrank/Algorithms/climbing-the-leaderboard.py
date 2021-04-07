#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    def rank(l,int1,high,low):
        x=high
        y=low
        if int1<list1[(x+y)//2]:
            if x==y:
                list_result.append(x+2)
            elif (x-y)==1:
                if int1>=list1[y] and int1>list1[x]:
                    list_result.append(y+1)
                if int1<list1[y] and int1>list1[x]:
                    list_result.append(x+1)
                if int1==list1[x]:
                    list_result.append(x+1)
                if int1<list1[x]:
                    list_result.append(x+2)
            else:
                return rank(l,int1,x,(x+y)//2)
        if int1>list1[(x+y)//2]:
            if x==y:
                list_result.append(x+1)
            elif x-y==1:
                if int1>=list1[y] and int1>list1[x]:
                    list_result.append(y+1)
                if int1<list1[y] and int1>list1[x]:
                    list_result.append(x+1)
                if int1==list1[x]:
                    list_result.append(x+1)
                if int1<list1[x]:
                    list_result.append(x+2)
            else:
                return rank(l,int1,(x+y)//2,y)
        if int1==list1[(x+y)//2]:
            list_result.append(((x+y)//2)+1)
          
    list1=[]
    list_result=[]
    list1=list(set(ranked))
    list1.sort(reverse=True)
    for score in player:
        rank(list1,score,len(list1)-1,0)
    return list_result

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
