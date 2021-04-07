#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[len(s)-2]=="P":
        if not ((int(s[0])*10)+int(s[1]))==12:
           intt=(int(s[0])*10)+int(s[1]) 
           return str(intt+12)+s[2:len(s)-2]
        return s[:len(s)-2] 
    else:
        if (int(s[0])*10)+int(s[1])==12 and s[len(s)-2]=="A" :
            return "0"+"0"+s[2:len(s)-2]
        return s[:len(s)-2]    
       
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
