# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:47:02 2023

@author: rahul
"""

s = "luffy is still joyboy"

t = len(s)
print(t)
print(s[-t])

temp = ""
tc = 0

for i in range(-1,-t,-1):
    print(i)
    temp += s[i]
    tc += 1
    if s[i] == " ":
        print("space")
        break
    
print(temp)
t1 = len(temp)
print(t1)
temp2 = ""
for j in range(-2,-len(temp)-1,-1):
    temp2 += temp[j]
    
print(temp2)
    