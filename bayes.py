# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:10:53 2017

@author: Shivam
"""
from __future__ import division
from collections import defaultdict

d=defaultdict(list)


start=int(input("how many choices are present?"))
#asks the user how to start the tree
count=0
#sets the count to zero to break the while loop further down
while start>0:
    count+=1
    #adds to the counter in the loop
    A=float(input('what is the probability of the initial event?'))#probability of the first event
    ask=int(input('how many possibilities are linked to this event?'))#linked probabilities
    #how many choices are linked to the first choice
    second=0#counter for the next loop
    tree=[]#makes a list of the linked probabilities
    while ask>0:#starts the loop
        second+=1
        B=float(input('what is the probability of the next event?'))
        tree.append(B)#adds each of the linked probabilities to the list
        if second==ask: #breaks the loop for all the linked probabilities
            break       
    d.setdefault(A, []).append(tree)    
    if count==start: #breaks the while loop altogether
        break

print(d)

#this gets P21 and P1 but we need P2
choice=float(input('what is the probability you want to start with?'))
#asks the user what event you want
if choice in d:
    #if the probability is in the dictionary
    print(d[choice])
    #print the linked probabilities
    decision=float(input('which outcome do you want'))
    #which one of these linked probabilities do you want

linked_to_choice=float(input('how many of the intial probabilities lead to the same outcome?'))

    
counter=0
denominator=[]
while linked_to_choice>0:
    if linked_to_choice:
        pass
    counter+=1
    second_A=float(input('what is the probability of the initial event?'))#probability of the first event
    if second_A in d:
        print(d[second_A])
        second_decision=float(input('which outcome do you want?'))
    denominator.append(second_A*second_decision)
    if counter==linked_to_choice:
        break
final_denominator=sum(denominator)
true_denominator=float(final_denominator)
        

P21=(decision)
P1=(choice)
print((P21*P1)/(true_denominator))

    








