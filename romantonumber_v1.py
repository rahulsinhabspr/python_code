# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:04:33 2023

@author: rahul
"""
roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

print(roman_dict['I'])

s = "MCMXCIV"
t = len(s)
print("length", t)

output = 0

for i in range(t-1):
    print(i, "test")
    print(s[i])
    print(s[i+1])
    print("initial", output)
    if s[i] == 'I' and s[i+1] == 'V':
        print("t1",i)
        print("output", output)
        output += -1
    elif s[i] == 'I' and s[i+1] == 'X':
        print("t2",i)
        print("output", output)
        output += -1        
    elif s[i] == 'X' and s[i+1] == 'L':
        print("t3",i)
        print("output", output)
        output += -10
    elif s[i] == 'X' and s[i+1] == 'C':
        print("t3",i)
        print("output", output)
        output += -10
    elif s[i] == 'C' and s[i+1] == 'D':
        print("t4",i)
        print("output", output)
        output += -100
    elif s[i] == 'C' and s[i+1] == 'M':
        print("t4",i)
        print("output", output)
        output += -100
    else:
        for j in roman_dict.keys():
            if j == s[i]:
                print(i, "test2",s[i])
                print("t5",i)
                print("output", output)
                output += roman_dict[j]
    
output += roman_dict[s[t-1]]

"""
    for j in roman_dict.keys():
        if j == i :
            print(roman_dict[j])
            output += roman_dict[j]
        if 
"""


          
print(output)