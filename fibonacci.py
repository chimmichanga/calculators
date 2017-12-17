# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 16:56:58 2017

@author: Shivam
"""

#Fibonacci sequence calculator
#fn=fn-1+fn-2

Number = int(input("\nPlease Enter the Range Number: "))
 
i = 0
First_Value = 0 
Second_Value = 1
           
# Find & Displaying Fibonacci series
while(i < Number):
           if(i <= 1):
                      Next = i
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next)
           i = i + 1