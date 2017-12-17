# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 02:27:34 2017

@author: Shivam
"""


def collatz(number): #defines the function
    count=0 #sets up a counter
    while number!=1: #initiates the while loop to prevent 1 from occurring
        if number %2==0: #checks if number is even
            number=(number/2) 
            print(number) #prints the even number divided by two and sends it back to the while loop
            count=count+1 #adds to the counter
        else: #if the number not even
            number= (3*number+1)
            print(number)
            count=count+1 #adds to the counter
    else: #outside the while loop prints the result
        print ('That took' + ' '+ str(count) +' ' +'steps') #tells us how many iterations were needed
        
def main(): #sets the function for using the input
    number=int(input('what is your number'))
    collatz(number) #calls the collatze function to the input

main()

'''This is a code which tests the collatz conjecture in mathematics.'''
