# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 19:36:50 2023

@author: rahul
"""

import string

print(string.ascii_letters)

############# Alphabet List #############################

l1 = string.ascii_letters
print(l1)
######### Number List ########################

N1 = []

for i in range(10):
    N1.append(str(i))
print(N1)


############################### Subsitution dknary ############

dknary = {}

for j in range(1,len(l1)-1):
    print(l1[j])
    if l1[j] == 'b':
        dknary[l1[j]]= 'a'
    else:
        dknary[l1[j]]= l1[j-1]
        
dknary['Z']='a'
dknary['a']='Z'
dknary['0']='9'

for i in range(1,len(N1)):
    if N1[i] == '9':
        dknary[N1[i]] = '0'
    else:
        dknary[N1[i]] = N1[i-1]

print(dknary)

################################### opening the encrpyted file #######################

z =''
with open("encrpyt_rahul.txt") as f:
    while True:
        c = f.read()
        if not c:
            print('End of file')
            break
        
        for i in c:
            if i == '#':
                z = z + ' '
            elif i == '*':
                z = z + '.'
            elif i == '@':
                z = z + "'"
            elif i == '&':
                z = z + "\n"
            else:
                z = z + dknary[i]
        
print(z)

    
###################### wrinting decrpted data in file ###############

file = open('decrpyt_rahul.txt',"w")
file.write(z)
file.close()




