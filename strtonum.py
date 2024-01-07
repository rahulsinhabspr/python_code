# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:04:33 2023

@author: rahul
"""
roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

a = str(121345)
print(a)
b = 1
d = 1
c = 0

print(len(a))

for i in range(len(a)):
    print('i',i)
    print('ii', -i)
    if i == 0:
        pass
    elif i == 1:
        c = int(a[-i])
    else:
        b = b  * 10
        print('b ', b)
        d = b * int(a[-i])  
        c += d
        print(c)
        


print(b)    
x = int(a[0]) * (10 *b)
print(x)
c = x + c    
print(a)
print('c')
print(c)

    


