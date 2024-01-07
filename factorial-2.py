# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:32:15 2023

@author: rahul
"""

def fact(n):
    if n == 0:
        return 1
    else:
        return (n * fact(n-1))
    
x = int(input('Enter the number to find factorial: '))

if x < 0:
    print('factorial of negative number is not possible')
else:
    print('factorial of given number is:  ',fact(x))