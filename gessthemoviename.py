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
    
    #print(movieName)
    print(maskedMovieName)

    # calculating maximum number of chance to be given to guess the movie name
    
    withoutSpaceMovieName = []

    for i in range(len(movieName)):
        #removing space from the name
        if movieName[i] != ' ':
            withoutSpaceMovieName.append(movieName[i])
        
    withoutSpaceMovieName.sort()
    #print('sorted Movie Name: ', withoutSpaceMovieName)

    nm1=[]

    for i in range(len(withoutSpaceMovieName)-1):
        if withoutSpaceMovieName[i]==withoutSpaceMovieName[i+1]:
            pass
        else:
            nm1.append(withoutSpaceMovieName[i])
        if (i+1)==(len(withoutSpaceMovieName)-1):
            nm1.append(withoutSpaceMovieName[i+1])
            
                
    #print('new list1: ', nm1)        

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
        if c < l :
            
            if c%2 == 0 :
                x = input('Player 1, it is your chance to select the letter: ')
                for i in range(len(movieName)):
                    if x == movieName[i]:
                        newmaskedMovieName[i] = x
                    
                    latestMaskedMovieName = latestMaskedMovieName + newmaskedMovieName[i]     
                print(latestMaskedMovieName)
                c = c + 1
                
                if latestMaskedMovieName == movieName:
                    print("Player1 you successfully guessed the movie")
            
    
    
    
                g = input('Do you want to continue 1 for Yes and 0 for No')
                g = int(g)
                if g == 0 :
                    d = d + 1
    
    
            else:
                y = input('Player 2, it is your chance now to select the letter: ') 
                for i in range(len(movieName)):
                    if y == movieName[i]:
                        newmaskedMovieName[i] = y
                    
                    latestMaskedMovieName = latestMaskedMovieName + newmaskedMovieName[i]
                print(latestMaskedMovieName)
                
                if latestMaskedMovieName == movieName:
                    print("Player1 you successfully guessed the movie")
                     
                
                
                g = input('Do you want to continue 1 for Yes and 0 for No')
                g = int(g)
                if g == 0 :
                    d = d + 1
                
    

guessTheMovie()