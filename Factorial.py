# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:29:53 2020

@author: Kirtan
"""

def fctrl(n):
    if n==0:
        return 1
     
    elif n==1:
        return 1
    
    elif n>=2:
        fact = 1
        for i in range (0,n):
            fact *= n
            n-=1
        return fact
    
num = int(input("Enter The Number : "))
print("Factorial of",num,"is", fctrl(num)) 