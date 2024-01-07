# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 15:47:52 2023

@author: rahul
"""

s = 'abaabaaba'

v = s[0]
lr = []
t1 = 0
t2 = 0
t3 = 0
substring = ''
for i in range(len(s)):
    if v == s[i]:
        lr.append(i)
for i in range((lr[1])):
    substring = substring + s[i]
for i in range(0,len(s),len(substring)):
    for j in range(len(substring)):
        if i+j < len(s):
            if s[i+j] == substring[j]:
                t2 += 1
            else:
                t3 += 1
                break
        else:
            t1 += 1
if t1 != 0:
    print('false-t1',t1)
if t3 != 0:
    print('false',t3)
if t2 !=0 and t1 == 0 and t3 == 0:
    print('true',t2)
       