# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 21:35:25 2023

@author: rahul
"""
nums = [1,2,2,2,2,2,3,3,3,3,4,4,4,5]

c = 0
d = 0


for i in range(len(nums)-1):
    print('i ',i)
    if nums[i+1] > nums[i]:
        print('value of i: ', i, 'values ', nums[i+1], 'Valuesii ', nums[i])
        c += 1
        print('value of c ', c)
    elif nums[i+1] < nums[i]:
        print('value of i: ', i, 'values ', nums[i+1], 'Valuesii ', nums[i])
        d += 1
        print('value of d ',d)
        
print('checking')
print(len(nums))
print(c)
print(d)
        
if ( c != 0 and d == 0) or (c == 0 and d != 0) or ( c == 0 and d == 0):
    print('monotonic array')
else:
    print('non-monotonic-array')