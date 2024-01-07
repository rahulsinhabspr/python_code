# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:12:40 2023

@author: rahul
"""

import numpy
board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
print(board)

p1s='X'
p2s='O'

def place(symbol):
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
    
l = range(3)

def check_diagonal(symbol):
    count = 0
    count2 = 0
    for i in l:
        if board[i][i] == symbol:
            count += 1
        if board[i][len(l)-1-i] == symbol:
            count2 += 1
               
    if count == 3 or count2 == 3:
        print(symbol + ' has won the game')
        return True
    return False

def check_row(symbol):
    for r in l:
        count = 0
        for c in l:
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(symbol + ' has won the game')
            return True
    return False

def check_col(symbol):
    for c in l:
        count = 0
        for r in l:
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(symbol + ' has won the game')
            return True
    return False


def won(symbol):
    return check_diagonal(symbol) or check_row(symbol) or check_col(symbol)
                                          
def play():
    for turn in range(9):
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