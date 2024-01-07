# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 16:42:44 2023

@author: rahul
"""

haystack = 'a'
needle = 'a'


if len(haystack) >= len(needle):
    t1 = 0
    t2 = 0
    for i in range(len(haystack)):
        t1 += 0
        z = 0
        print('r',i)
        if haystack[i] == needle[0]:
              print('rahul',i)
              z = i
              c = 0
              for j in range(len(needle)):
                  print('s',i+j)
                  if i+j < len(haystack):
                      print('rs',i+j)
                      if haystack[i+j] == needle[j]:
                          c += 1
                          print(c,haystack[i+j],needle[j])
              if c == len(needle):
                   print('got it')
                   print('Desired output: ', z)
                   break
              else:
                  t2 += 1
                  print('last - -1',t2)           
        else:
            t1 += 1
    if t1 == len(haystack):
        print('t1 -1')
    if t2 != 0:
        print('t2', t2)
else:
    print('-1')
                  


    