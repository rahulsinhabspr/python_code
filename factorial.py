# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:13:17 2023

@author: rahul
"""
def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product


n = int(input('Please enter the positive number to calculate factorial: '))
if n >= 0:
    y= factorial(n)
    print('The factorial of ',n ,' is ', y)
else:
    print('Entered number is Negative Number, Factorial od Negative Number do not Exist.')