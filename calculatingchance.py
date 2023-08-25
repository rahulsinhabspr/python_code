# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 15:07:23 2023

@author: rahul
"""
    
    
    
"""
    for j in range(i+1,len(a)):
        print(i,j)
        print(a[i],a[j])
        if a[i]==a[j]:
            u=u+1
            print(i,a[i],j,a[j])
            

print(u)
"""

import random

movielist = ['the sand of time','guardians of the galaxy vol 3','pyar kiya to darna kya','ramayan','gadar','gadar 2','hum aapke hain koun', 'anand','kuch kuch hota hai']
moviepick = random.choice(movielist)
print(moviepick)

u=0
u=int(u)

s=0
s=int(s)

wsm=[]

print('Length of the movie pick: ', len(moviepick))

for i in range(len(moviepick)):
    #removing space from the name
    if moviepick[i]== ' ':
        print('space exist in this position', i)
        s=s+1
    else:
        print('without space',moviepick[i])
        wsm.append(moviepick[i])
        
print('without space:',wsm)
wsm.sort()
print('sorted wsm: ', wsm)

nm=[]
nm1=[]
for i in range(len(wsm)-1):
    nm.append(wsm[i])
    if wsm[i]==wsm[i+1]:
        print('if:', i)
    else:
        print(i)
        nm1.append(wsm[i])
    if (i+1)==(len(wsm)-1):
        print('rahul')
        nm1.append(wsm[i+1])
            
print(moviepick)        
print('value of space',s)

print('new list1: ', nm1)        

no=len(nm1)
print('Maximum number of spaces', no)







