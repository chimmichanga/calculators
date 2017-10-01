# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:10:53 2017

@author: Shivam
"""


i=int(input("how many outcomes are there for the first part?"))
piece=0

init_prob=[]
while piece<i:
    piece+=1
    prob1=float(input('what is the probability'))
    init_prob.append(prob1)
print(init_prob)
length=(len(init_prob))


for u in range(length):
    s=int(input('how many outcomes are there for the second part?'))
    sec_prob=[]
    for x in range(s):
        prob2=float(input('what is the probability?'))
        sec_prob.append(prob2)
    print(sec_prob)
    







