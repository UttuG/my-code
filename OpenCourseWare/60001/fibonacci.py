# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 08:34:45 2020

@author: Stalik
"""
#exceptional handling
#no of iterations
#both
def fib(x,dic):
    if x in dic:
        return dic[x]
    else:
        ans=fib(x-1, dic)+fib(x-2, dic)
        dic[x]=ans
        return ans
dic={0:0,1:1,2:1}
x=int(input("Type your number:"))
print(fib(x,dic))
print(fib(x,dic)/fib(x-1,dic))