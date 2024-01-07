# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 00:19:00 2023

@author: rahul
"""

a = 'rahulr'
b = 'rahul'


a1 = {}
b1 = {}

for i in b:
    
    d = 0
    for j in b:
        if i == j:
            d += 1
            a1[i]=d
            
    c = 0
    for j in a:
        if i == j:
            break
        else:
            c += 1
    if c == len(a):
        print('che',i)


print(a1)