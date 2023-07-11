# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:22:31 2020

@author: Kirtan
"""

import random
play = "y"
while play == "y":
    
    print("Number on the dice is : ",random.randint(1,6))
    print()
    p=input("Play More? (Y) :")
    if p.lower()!="y":
        play="n"
        break