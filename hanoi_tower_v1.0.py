# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 19:42:39 2020

@author: Stalik
"""
#Suggestions for v2.0(introduction to colour printing on python)
    #total no of moves
    #color towers on print(p1/p2/p3 color coding)
#Suggestions for v3.0(Graphical rep of hanoi towers)
    #Actually able to display the towers and movement on shell using carriage return
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
p1disks=int(input("no of disks in tower 1?"))
print(Towers(p1disks, 'P1', 'P2', 'P3'))

