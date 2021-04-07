#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    obs_n=[]
    obs_s=[]
    obs_e=[]
    obs_w=[]
    obs_ne=[]
    obs_se=[]
    obs_nw=[]
    obs_sw=[]
    for i in obstacles:
        if i[0]-r_q==i[1]-c_q and i[0]-r_q>0:
            obs_ne.append(i)
        if i[0]-r_q==i[1]-c_q and i[0]-r_q<0:
            obs_sw.append(i)
        if abs(i[0]-r_q)==abs(i[1]-c_q) and (i[1]-c_q)>(i[0]-r_q):
            obs_se.append(i)
        if abs(i[0]-r_q)==abs(i[1]-c_q) and (i[1]-c_q)<(i[0]-r_q):
            obs_nw.append(i)
        if i[0]==r_q and i[1]-c_q>0:
            obs_e.append(i)
        if i[0]==r_q and i[1]-c_q<0:
            obs_w.append(i)
        if i[1]==c_q and i[0]-r_q>0:
            obs_n.append(i)
        if i[1]==c_q and i[0]-r_q<0:
            obs_s.append(i)
    try :
        cne=obs_ne[0]
        for x in obs_ne:
            if ((x[1]-c_q))<=((cne[1]-c_q)):
                cne=x
    except: 
        pass
    try:
        cse=obs_se[0]
        for x in obs_se:
            if ((x[1]-c_q))<=((cse[1]-c_q)):
                cse=x
    except:
        pass
    try:
        cnw=obs_nw[0]
        for x in obs_nw:
            if ((x[0]-r_q))<=((cnw[0]-r_q)):
                cnw=x
    except:
        pass
    try:    
        csw=obs_sw[0]
        for x in obs_sw:
            if ((x[0]-r_q)**2)<=((csw[0]-r_q)**2):####
                csw=x
    except:
        pass
    try:
        cn=obs_n[0]
        for x in obs_n:
            if ((x[0]-r_q))<=((cn[0]-r_q)):
                cn=x
    except:
        pass
    try:
        ce=obs_e[0]
        for x in obs_e:
            if ((x[1]-c_q))<=((ce[1]-c_q)):
                ce=x
    except:
        pass
    try:           
        cs=obs_s[0]
        for x in obs_s:
            if ((x[0]-r_q)**2)<=((cs[0]-r_q)**2):
                cs=x
    except:
        pass
    try:
        cw=obs_w[0]
        for x in obs_w:
            if ((x[1]-c_q)**2)<=((cw[1]-c_q)**2):####
                cw=x
    except:
        pass
    try:
        n_moves=min(abs(cn[0]-r_q)-1,abs(n-r_q))
    except:
        n_moves=abs(n-r_q) 
    try:
        s_moves=min(abs(cs[0]-r_q)-1,abs(r_q-1)) 
    except:
        s_moves=abs(r_q-1)  
    try:
        e_moves=min(abs(ce[1]-c_q)-1,abs(n-c_q))
    except:
        e_moves=abs(n-c_q) 
    try:
        w_moves=min(abs(cw[1]-c_q)-1,abs(c_q-1)) 
    except:
        w_moves=abs(c_q-1)  
    try:
        nw_moves=min(abs(cnw[0]-r_q)-1,abs(n-r_q),abs(c_q-1))
    except:
        nw_moves=min(abs(n-r_q),abs(c_q-1))
    try:
        sw_moves=min(abs(csw[0]-r_q)-1,abs(r_q-1),abs(c_q-1))
    except:
        sw_moves=min(abs(r_q-1),abs(c_q-1))
    try:
        ne_moves=min(abs(cne[0]-r_q)-1,abs(n-r_q),abs(n-c_q))
    except:
        ne_moves=min(abs(n-r_q),abs(n-c_q))
    try:
        se_moves=min(abs(cse[0]-r_q)-1,abs(r_q-1),abs(n-c_q))
    except:
        se_moves=min(abs(r_q-1),abs(n-c_q))
   
    return n_moves + s_moves + e_moves + w_moves + se_moves + ne_moves + sw_moves + nw_moves
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
        
    fptr.write(str(result) + '\n')

    fptr.close()