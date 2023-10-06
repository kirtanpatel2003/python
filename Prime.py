# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:09:54 2020

@author: Kirtan
"""

def prime(x):
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                print(x,"is not a prime number")
                break
            else:
                print(x,"is a prime number")
    else:
        print(x,"is not a prime number")
n= int(input("Enter The Number : "))
prime(n)
