# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 11:29:46 2023

@author: rahul
"""

import random

#masked the movie name
def maskedMovieName(movieName):
    maskedMovieName=''
    for i in range(len(movieName)):
        if movieName[i] == ' ':
            #print('position of space ', i)
            maskedMovieName = maskedMovieName + ' '
        else:
            #print(i, " ", movieName[i])
            maskedMovieName = maskedMovieName + '*'
    return maskedMovieName
    

###################################
# calculating maximum number of chance to be given to guess the movie name
def maxChances(movieName):
    
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
    return (int(len(nm1)))
#########################################

def pickMovie():
    movielist= ['the sand of time','guardians of the galaxy vol 3','pyar kiya to darna kya','ramayan','gadar','gadar 2','hum aapke hain koun', 'anand','kuch kuch hota hai','avengers','saajan']
    movieName= random.choice(movielist)
    return movieName

#############################################################################
def guesstheMovieName():
    return ('total point 10')

#####################################################################

######################################################################

# guesstheMovieName()

##########################################################

# plr1Name = input('Player 1, What is your Name ')
# plr2Name = input('Player 2, What is your Name ')

plr1Points = 0
plr2Points = 0

plr1play = int(input('Player 1, Do you want to play: 1 for Yes and 0 for No '))
plr2Play = int(input('Player 2, Do you want to play: 1 for Yes and 0 for No '))

if (plr1play == 1) and (plr2Play == 1):

    movieName = pickMovie()
    print(movieName)

    #masked the movie name
    maskedMovie = maskedMovieName(movieName)
    print(maskedMovie)
                                                                                                                                                                                             
    #Maximum Number of chances
    l = maxChances(movieName)
    
    movieletter = []
    
    for i in movieName:
        if i == ' ':
            movieletter.append(i)
        else:
            movieletter.append(i)
            
    
    c=1
    
    maskedmovieLetter = []
    
    for i in maskedMovie:
        maskedmovieLetter.append(i)
    
    
    
    while c==1:
        x = input('Player 1, it is your chance to select the letter: ')
        nm = []
        for i in range(len(movieletter)):
            if x == movieletter[i]:
                maskedmovieLetter[i]=x
                plr1Points = plr1Points + 10
        
        nMM = ''
        for i in range(len(maskedmovieLetter)):
            nMM = nMM + maskedmovieLetter[i]
        
        print(nMM)
        print(plr1Points)
        
        if nMM == movieName:
            break
    
        
    
        y = input('Player 2, it is your chance to select the letter: ')
        
        for i in range(len(movieletter)):
            if y == movieletter[i]:
                maskedmovieLetter[i]=y
                plr2Points = plr2Points + 10
        
        nMM = ''
        for i in range(len(maskedmovieLetter)):
            nMM = nMM + maskedmovieLetter[i]
        
        print(nMM)
        print(plr2Points)
            
        
        
        if nMM == movieName:
            c=2
        
    
else:
    print('Thank you')
