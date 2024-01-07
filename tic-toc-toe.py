# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:12:40 2023

@author: rahul
"""

import numpy
board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
print(board)

########## Testing #################
"""
print(board[2][2])

board[2][2] = 'Ra'

print(board)
"""

p1s='X'
p2s='O'

def place(symbol):
    print(symbol)
    i = 0
    while i == 0:
        r = int(input('Please select row between 1 to 3: '))
        c = int(input('Please select col between 1 to 3: '))
        
        if (r > 0 and r < 4) and (c > 0 and c < 4) and (board[r-1][c-1] == '-'):
            break
        else:
            print('Invalid input, try again')
    board[r-1][c-1] = symbol
    print(board)
    

def won(player):
    ### 1 row
    
    """
    for i in range(3):
        a = ''
        for j in range(3):
            a = a + board[i][j]
        print(a)
        if a == 'XXX':
            print(player, 'Won')
            return True
        elif a == 'OOO':
            print(player , 'won the game')
            return True
        else:
            pass
        
    """
    if (board[0][0] == player ) and (board[0][1] == player ) and (board[0][2] == player ):
        print(player + ' has won the game')
        return True
    if (board[1][0] == player ) and (board[1][1] == player ) and (board[1][2] == player ):
        print(player + ' has won the game')
        return True
    if (board[2][0] == player ) and (board[2][1] == player ) and (board[2][2] == player ):
        print(player + ' has won the game')
        return True
    
    ##  2 col
    if (board[0][0] == player ) and (board[1][0] == player ) and (board[2][0] == player ):
        print(player + ' has won the game')
        return True
    if (board[0][1] == player ) and (board[1][1] == player ) and (board[2][1] == player ):
        print(player + ' has won the game')
        return True
    if (board[0][2] == player ) and (board[1][2] == player ) and (board[2][2] == player ):
        print(player + ' has won the game')
        return True
    ## 3 diaganol
    if (board[0][0] == player ) and (board[1][1] == player ) and (board[2][2] == player ):
        print(player + ' has won the game')
        return True
    if (board[0][2] == player ) and (board[1][1] == player ) and (board[2][0] == player ):
        print(player + ' has won the game')
        return True
    
def play():
    for turn in range(9):
        print(turn)
        if turn%2 == 0:
            print('X your turn')
            place(p1s)
            if won(p1s):
                break
        else:
            print('O your turn')
            place(p2s)
            if won(p2s):
                break
        turn += 1
        
    if not(won(p1s)) and not(won(p2s)):
        print('Match Draw')

play()