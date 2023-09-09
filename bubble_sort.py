# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 01:46:14 2023

@author: rahul
"""


m = [5,3,4,9,8,10,19,2,6,7,11,1]
print('Length of m list: ',len(m))

n = []

for i in range(len(m)):
    print('i',i)
    for j in range(len(m)-i-1):
        print('j',j)
        tmp = m[j+1]
        if m[j] > m[j+1]:
            m[j+1] = m[j]
            m[j]=tmp
            print(m)
            
            
print(m)

