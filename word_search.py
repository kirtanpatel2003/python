# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:40:59 2020

@author: Kirtan
"""

def countWrd(strg,word):
    s = strg.split()
    count=0
    for w in s:
        if w==word:
            count+=1
    return count

strg = str(input("Enter The String : ")) 
word = str(input("Enter The Word : "))
a = strg.find(word)
l=len(word)
f = strg[a:a+l]
count=countWrd(strg,word)
if f == word:
    print("",word," occurs ",count," times...")
else:
    print("Word Not Found")