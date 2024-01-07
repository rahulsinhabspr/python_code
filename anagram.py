# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 13:24:25 2023

@author: rahul
"""

s = 'rat'
t = 'car'

if len(s) == len(t):
    sl = []
    tl = []
    for i in range(len(s)):
        sl.append(s[i])
        tl.append(t[i])
    sl.sort()
    tl.sort()
    print(sl)
    print(tl)
    if sl == tl:
        print('True')
    else:
        print('NotSame False')
    
    
else:
    print('False')