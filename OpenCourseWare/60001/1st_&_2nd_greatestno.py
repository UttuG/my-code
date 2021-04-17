# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 09:26:49 2020

@author: Stalik
"""
#could have used max function and also sorting in the list.highly efficent but kinda cheating
#REMEMBER TO CHECK THE DATA TYPE OF LIST!STRING CAN COMPARE NUMBERS OF SAME LENGTH!BE AWARE! 
numlist=[]
while True:
    i=input("Enter your number:")
    #could have used exception handling but would have been long
    if i.isdigit():
        numlist.append(int(i))
    else:
        break
if numlist[0]>numlist[1]:
    _max=numlist[0]
    _max2=numlist[1]
else:
    _max=numlist[1]
    _max2=numlist[0]
for n in numlist[2:len(numlist)]:
    if n > _max:
        _max2=_max
        _max=n
    elif n > _max2:
        _max2=n
    
print("Greatest no:",_max,"\n"+"Sceond Greatest no:",_max2,"\n","\n")    
