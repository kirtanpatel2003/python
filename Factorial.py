# -*- coding: utf-8 -*-
"""
Created on Wed Dec 2 21:29:53 2020

@author: Kirtan
"""

def num_factorial(n):
    """
    Calculate the factorial of a given number.

    Parameters:
        n (int): The input number.

    Returns:
        int: The factorial of the input number.
    """
    if n == 0:
        return 1
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter The Number : "))
print("Factorial of", num, "is", fctrl(num))
