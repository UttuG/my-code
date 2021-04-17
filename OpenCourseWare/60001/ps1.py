# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:13:14 2020

@author: Stalik
"""
annual_salary=float(input("What's your annual salary?"))
saved=float(input("How much of it do you want to save?"))
interest=float(input("What's the annual rate of growth of savings?"))
cost=float(input("What's the cost of the house?"))
down_pay=float(input("How much of it is the down payment?"))
semia_raise=float(input("How much is the semi annual raise?"))
down=down_pay*cost
current_savings,i= 0.0,0.0
while(current_savings<down):
    i +=1
    current_savings += current_savings*(interest/12)+(annual_salary*saved) 
    if(i%6==0):
        annual_salary += annual_salary*semia_raise
        break
print("The numbers of months you have to save are", i)
    
    

