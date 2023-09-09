# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:19:42 2023

@author: rahul
"""

############## creating empty list ###################

a = []

print(a)

######### adding values to the list ##############################

for i in range(101):
    a.append(i)
    
print(a)

########################### slicing list  ############################
b = a[2:7]
print("Slicing List")
print(b)

c = a[8:100:10]
print("Slicing List")
print(c)

d = str(c[2])  
print(d)
print(d[1])

 ################ calculating the sum of digit ################
 
def sum_Total(x):
    y = str(x)
    sumTotal = 0
    for i in y:
        sumTotal += int(i)
    return sumTotal


print('Sum of digit:', sum_Total(123))
 