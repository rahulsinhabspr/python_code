# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 12:01:07 2023

@author: rahul
"""

l1=[]
l2=[]

for i in range(1,21):
    l1.append(i)
    if i%3 == 0 and i%5 == 0 :
        print('FizzBuzz')
        l2.append('FizzBuzz')
    elif i%3 == 0 :
        print('Fizz')
        l2.append('Fizz')
    elif i%5 == 0 :
        print('Buzz')
        l2.append('Buzz')
    else :
        print(i)
        l2.append(i)

print(l1)
print(l2)