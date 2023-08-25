# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 22:01:22 2023

@author: rahul
"""

l1=[1,2,1,54,99,877,56,43,65,554,124,1,2,3,1,4,1000,550,65,24,42,32,84,11,15,12,13,14,15,1,4,85,78,1,1,5,6,7,8,9,1,1,400,405]
print('given list : ',l1)

l=len(l1)
print('length of the list :: ',l)



l2=l1
l2.sort()
print('sorted list : ',l2)

l3=l1
l3.reverse()
print('reverse sorted list : ',l3)

x=l1.count(1)
print('couting particular item 1 in list',x)

print(l1)

l4=l1
l4=l4[:10]
print('slicing the list from begening to 10 item',l4)

l5=l1
l5=l5[2:10]
print('slicing the list from position 2 to 10',l5)

l6=l1
y=10
l6.insert(0, y)
print('inserting 10 new item in the first position of list')
print(l6)


l7=l1
l7.append(9000)
print('new length of the list after appending it',len(l7))
print(l7)
    
