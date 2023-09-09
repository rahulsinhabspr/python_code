# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 16:09:32 2023

@author: rahul
"""

a = []

for i in range(120):
    a.append(i)


def binary_search(a,x):
    first_position = 0
    last_position = len(a)-1
    number_found = 0

    while first_position <= last_position and number_found == 0:
        mid = (first_position + last_position)//2
        if x == a[mid]:
            number_found = 1
            print("The requested number is : " +  str(a[mid]))
            return  
        else:
            if x > a[mid]:
                first_position = mid + 1
                print('Number not in between:', first_position,last_position)
                print(mid)
            else:
                last_position = mid - 1
                print('Number not in between:', first_position,last_position)
                print(mid)

x = int(input('User select any number between 0 to 119:: '))

binary_search(a, x) 
        