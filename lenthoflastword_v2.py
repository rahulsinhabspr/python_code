# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:47:02 2023

@author: rahul
"""

s = "luffy is still joyboy"

t = len(s)
print(t)
print(s[-t])

temp = 0

for i in range(t):
    print(i,"Sequence Number")
    if s[i] == " ":
        print("Space Position")
        print("Temporary Position", i)
        temp = i
    
print(temp)
temp2 = ""


for j in range(temp+1,t,1):
    print(j)
    print(s[j])
    temp2 += s[j]
    
print(temp2)

print(len(temp2))

substring_last = s[temp+1:]

print(substring_last)