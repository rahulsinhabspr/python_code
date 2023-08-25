# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 13:23:06 2023

@author: rahul
"""

def guessTheMovie():

    import random
    
    movielist= ['the sand of time','guardians of the galaxy vol 3','pyar kiya to darna kya','ramayan','gadar','gadar 2','hum aapke hain koun', 'anand','kuch kuch hota hai','avengers','saajan']
    movieName= random.choice(movielist)
    
    #masked the movie name 
    maskedMovieName=''
    for i in range(len(movieName)):
        if movieName[i] == ' ':
            #print('position of space ', i)
            maskedMovieName = maskedMovieName + ' '
        else:
            #print(i, " ", movieName[i])
            maskedMovieName = maskedMovieName + '*'
    
    print(movieName)
    print(maskedMovieName)

    # calculating maximum number of chance to be given to guess the movie name
    
    withoutSpaceMovieName = []

    for i in range(len(movieName)):
        #removing space from the name
        if movieName[i] != ' ':
            withoutSpaceMovieName.append(movieName[i])
        
    withoutSpaceMovieName.sort()
    print('sorted Movie Name without Space: ', withoutSpaceMovieName)

    nm1=[]

    for i in range(len(withoutSpaceMovieName)-1):
        if withoutSpaceMovieName[i]==withoutSpaceMovieName[i+1]:
            pass
        else:
            nm1.append(withoutSpaceMovieName[i])
        if (i+1)==(len(withoutSpaceMovieName)-1):
            nm1.append(withoutSpaceMovieName[i+1])
            
                
    print('new list1: ', nm1)        

    l=int(len(nm1))
    print('Maximum number of chances', l)


    #Players Name and desire to play Game
    
    # d = input('Do you want to play of guessing the Movie Name, please input 1 for Yes and 0 for no: ')
    
    
    #plr1 = input('Player1, What is your Name ')
    #Plr2 = input('Player2, What is your Name ')
    
    #plr1point = int(0)
    #plr2point = int(0)
    
    c = int(0)
    d = input('Do you want to play the Game of guessing the Movie Name, please input 1 for Yes and 0 for no: ')
    d=int(d)
    
    # converting movie name into list
    newmaskedMovieName = []
    for i in maskedMovieName:
        newmaskedMovieName.append(i)
        
    print(newmaskedMovieName)    
    latestMaskedMovieName = ''        
    
    while d == 1:
        print('maximum number of choice', l)
        for i in range(l):
            print('Players if you guess the movie in 1 attempt you will get maximum point, 100 ')
            
            
            
            
            
            print('Player 1, it is your turn to tell us your choice')
        
    print('Thank you for your time')
    
    
    
    

"""
    for i in range(l):
        if d == 0:
            break
        else:
            print(i)
            if c%2 == 0 :
                print('player1')
                c = c + 1
                x = input ('Player 1, please enter your choice')
                if x == ''
                
            else:
                print('player-2')
         
"""

guessTheMovie()