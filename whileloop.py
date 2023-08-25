# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 12:45:09 2023

@author: rahul
"""

# while loop 

print('Welcome to While loop checking')

c=1
ls =[]

while c==1 :
    t= input('Do you want to continue: Yes/No')
    if t=='Yes' :
          patient = input('what is your Name')
          ls.append(patient)
    else :
        c=2
    
    
print(ls)