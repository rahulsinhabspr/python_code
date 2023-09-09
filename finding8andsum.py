# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 18:20:04 2023

@author: rahul
"""

#### find total number  which has 8 in it from 1 to 100 and then find the total sum ############

a = []

for i in range(1,101):
    a.append(i)
    
print('Total List')
print(a)


##### printing 8 from 1 to 80 #############################
b = a[7:80:10]
# print(b)

######## printing 80 to 89 ###########################
c = a[79:89]
# print(c)

############## printing 89 to 101 ######################
d = [98]

# list of 8 number between 1 to 100
print('list of 8 number between 1 to 100')
f = b + c + d

print(f)

sum_Total = 0

for i in f:
    sum_Total += i
    
# The total sum of number in the list
print('The total sum of number in the list')
print(sum_Total)

###########################################################################################################


