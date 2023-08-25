# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:27:55 2023
import random
a='rahul'
print(a)
for i in a :
    print(i)

b = []
c=''

for i in range(len(a)) :
    b.append(a[i])
    c = c + a[i]

print(c)

print(b)

z= a[1]+a[2]

print(z)



q= random.sample(c,len(c))
p=''


for i in range(len(c)) :
    p = p + q[i]

print(p)

@author: rahul
"""

import random

wordlist = ['rahul','sejal','megha','taruna','swati','rani','papa','rahul sinha'] 
pickword=random.choice(wordlist)
q= random.sample(pickword,len(pickword))

p= ''
for i in range(len(q)) :
    p = p + q[i]
    

a= input('what is the your Name: ')
b=input('Do you want to play the guess the work game : Yes/No')

while b == 'Yes' :    
    print('Guess the word : ', p)
    x=input('chance : ')    
    if x== pickword :
        print('u guessed it right')
        b= 'No'
    else :
        y= input('Do u want to continue: Yes/No')
        if y== 'No' :
            b='No'
            
print('Game Completed')


