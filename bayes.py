# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:10:53 2017

@author: Shivam
"""

from collections import defaultdict

d=defaultdict(list)

start=int(input("how many choices are present?"))
count=0
while start>0:
    count+=1
    A=float(input('what is the probability of the first set of events?'))
    
    ask=int(input('how many possibilities are linked to the individual events?'))
    
    second=0
    
    tree=[]
    while ask>0:
        second+=1
        B=float(input('what is the probability?'))
        tree.append(B)
        if second==ask:
            break
    
   
    d.setdefault(A, []).append(tree)    

    if count==start:
        break

print(d)
    








