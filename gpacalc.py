# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:43:36 2017

@author: Shivam
"""

mylist=[]
i=int(input("how many classes did you take this term"))
x=0
c=0
real=0

while x<i:
    x+=1
    g=int(input('how many credits was the class'))
    d=0
    while d<g:
        d+=1
    c+=g
    
    grade1=input('What is the grade for the class?')     
    
    dictionary={'A':4,'B+':3.5,'B':3,'C+':2.5,'C':2,'D':1,'F':0}
    if grade1=='A':
        s=(dictionary[grade1]*g)
        
    if grade1=='B+':
        s=(dictionary[grade1]*g)
        
    if grade1=='B':
        s=(dictionary[grade1]*g)

    if grade1=='C+':
        s=(dictionary[grade1]*g)

    if grade1=='C':
        s=(dictionary[grade1]*g)

    if grade1=='D':
        s=(dictionary[grade1]*g)

    if grade1=='F':
        s=(dictionary[grade1]*g)


    mylist.append(s)
mist=sum(mylist)
        
print('The toal number of credits is',c)
print('The total credit hours are',mist)
print('Your GPA is',float(mist/c))

if i==0:
    print('there is nothing to calculate')
    
    


