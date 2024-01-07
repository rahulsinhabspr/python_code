# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 13:54:58 2023

@author: rahul
"""

l = [-1,-2,-3,-4,3,2,1]
prop = 1

for i in l:
    prop *= i
    
print('Product',prop)

if prop > 0 :
    print('Product is positive +')
elif prop < 0 :
    print('Product is Negative -')
else:
    print('Product is Zero 0')
    
    