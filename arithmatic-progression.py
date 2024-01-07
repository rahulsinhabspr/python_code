# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:56:15 2023

@author: rahul
"""


i = [1,2,4]

print('maxvalue', max(i))
print('minimum', min(i))

for k in range(len(i)):    
    for j in range(len(i)-1):
        temp = i[j]
        if i[j+1] < i[j]:
            i[j] = i[j+1]
            i[j+1] = temp
            
print(i)

d = i[1] - i[0]

print('common diff ',d )
c = 0

for j in range(1,len(i)-1):
    print('j ',j)
    p = i[j+1] - i[j]
    print('common difference ',p)
    if d != p:
        c += 1
        print('difference ', d , 'this difference ',p)
        
if c == 0:
    print('AP')
else:
    print('No Ap')
        
    