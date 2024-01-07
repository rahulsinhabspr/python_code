# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 15:47:52 2023

@author: rahul
"""

s = 'abaababaab'

t = []
v = s[0]
substring = ''

print(s)
print(len(s))

for i in range(len(s)-1):
    print(i)
    if v == s[i] and s[i] != s[i+1]: 
        print('ra',i)
        t.append(i)
    else:
        print('starting no repeatation')
        
print(t)


if len(t) > 1:
    for i in range((t[1])):
        print('t',i)
        print('t',s[i])
        print('t',t[1])
        substring = substring + s[i]
 
if len(substring) == 0:
    substring = substring + s[0]
print(substring)
print('substring length', len(substring))

t1 = 0
t2 = 0
t3 = 0

for i in range(0,len(s),len(substring)):
    print('i',i)
    for j in range(len(substring)):
        
        if i+j < len(s):
            if s[i+j] == substring[j]:
                t3 += 1
                print('rahul',i,j,i+j)
            else:
                t1 += 1
                break
        else:
            t2 += 1

if t2 != 0:
    print('t2--no repeation',t2)


if t1 != 0:
    print('no repeation')


if t3 != 0 and t1 == 0 and t2 == 0:
    y = t3/len(substring)
    print('Number of repetation is: ', y,' t3 ',t3, ' length of substring ', len(substring))


"""
for i in range(len(t)-1):
    print(t[i])
    print(t[i+1])
    print(i)
    for j in range(t[i],t[i+1]):
        print('insideloop : ',j)
"""      
        
