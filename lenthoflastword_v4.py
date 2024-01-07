# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:47:02 2023

@author: rahul
"""

s = " a"

t = len(s)
print("len",t)
print(s[-1])
print(s[-t])

temp = 0
tc = 0

if t > 1 :
    for i in range(-1,-t,-1):
        print(i)
        print(s[i])
        if s[i] != " ":
            tc += 1
        if i == -t + 1:
            print("checking zeroth position")
            if s[0] != " ":
                tc += 1
            
        if s[i] != " " and s[i-1] == " ":
            print("rahul sinha ")
            break        
    print(tc)      
else:
    print(t)
        


    



"""
for i in range(-1,-t,-1):
    print("Rahul Sinha")
    print("i", i)
    print(s[-i])
    if s[-i] != " ":
        tc += 1
        print("tc", tc)
    if s[i] != " " and s[i+1] == " ":
        print("Non-Space and Space")
        break
print(tc-1)


"""



"""

for i in range(-1,-t,-1):
    print("rahul")
    print(s[i])
    print(i)
    if s[i] != " ":
        tc += 1
        print("tc",tc)
    if s[i] == " " and s[i+1] != " ":
        print("space and non-space")
        temp = i
        break
        

print("Nonzero",tc)
print("lastpositionofSpace",temp)

if temp == 0:
    print(s)
else:
    t1 = t+temp+1
    print(t1)
    substring_last = s[t1:t1+tc]
    print(substring_last)
    print(len(substring_last))
    
"""  