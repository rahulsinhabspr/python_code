# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:46:19 2023

@author: rahul
"""

def guess():

    import random
    
    movielist= ['the sand of time','guardians of the galaxy vol 3','pyar kiya to darna kya','ramayan','gadar','gadar 2','hum aapke hain koun', 'anand','kuch kuch hota hai','avengers','saajan']
    movieName= random.choice(movielist)
    
    print(movieName)
    
    z=''
    for i in range(len(movieName)):
        if movieName[i] == ' ':
            print('position of space ', i)
            z=z + ' '
        else:
            print(i, " ", movieName[i])
            z=z+'*'
       
    print(z)

    q=len(movieName)
    print(q)

    #calculating total number of chances to be given to players


    plr1=input('Player1 : What is your Name: ')
    plr2=input('Player2 : What is your Name')
    p1point=0
    p2point=0
    
    c=1
    
    while c==1 :
        d=input('Do you want to play the game: Guess the Movie? 1/0 ')
        print(d)
        print(c)
        if d=='0':
            print('Thank you for your time')
            c=0
            print(c)
        else:
            print(plr1, ',guess the movie')
            print(z)
            x= input('Enter the letter')
        





guess()