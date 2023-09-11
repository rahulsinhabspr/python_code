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

for j in range(len(l1)):
    print(l1[j])
    if l1[j] == 'Z':
        dknary[l1[j]]= 'a'
    else:
        dknary[l1[j]]= l1[j+1]

for i in range(len(N1)):
    if N1[i] == '9':
        dknary[N1[i]] = '0'
    else:
        dknary[N1[i]] = N1[i+1]


print(dknary)


"""
######### Testing subsitution #####################

x = input('Please enter the word to encrpt: ')

y = ''

for i in x:
    if i == ' ':
        y = y + '###'
    else:
        y = y + dknary[i]
print(y)
"""
#################################### opening the file #######################
z =''
with open("rahul.txt") as f:
    while True:
        c = f.read()
        if not c:
            print('End of file')
            break
        print(c)
        print(c[27])
        print(c[28])
        print(c[29])
        print(c[30])
        print(c[31])
        print(c[32])
        print("'")
        
        for i in c:
            if i == ' ':
                z = z + '#'
            elif i == '.':
                z = z + '*'
            elif i == "'":
                z = z + '@'
            elif i == "\n":
                z = z + '&'
            else:
                z = z + dknary[i]
        
print(z)

###################### wrinting encrpting data in file

file = open('encrpyt_rahul.txt',"w")
file.write(z)
file.close()





