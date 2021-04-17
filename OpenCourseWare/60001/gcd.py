# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def gcd(x,y):
    if x==0:
        return y
    if y==0:
        return x
    if x>=y:
        return gcd(x%y, y)
    if y>x:
        return gcd(x, y%x)
num1=int(input("enter number 1:"))
num2 =int(input("enter number 2:"))
print(gcd(num1,num2))