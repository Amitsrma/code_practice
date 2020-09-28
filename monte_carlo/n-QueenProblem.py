'''
this is code to find the solution to N-queen problem

There are N queens placed in a NxN chessboard

The program should find a way to return the position of each of the queen
suchthat none of the queen threatens other.
'''

import random
import numpy as np

def makeBoard(n):
    '''
    this function takes the size of board as the argument 
    returns the list of list where each entry of the list is the position in the
    board
    '''
    board = []
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            posn = [i]
            posn.append(j)
            board.append(posn)
    return board

def eliminateOverlaps(position, board, n):
    '''
    this function takes the position with respect to which the other
    positions on the chess board that cannot be occupied by queens are
    eliminated.
    position: current position with respect to which the positions that cannot
    be occupied by other queen is eliminated
    board: the posiions available in the chess board
    n: represents the size of board (n x n)
    '''
    boardCopy = board.copy()
    for posn in board:
        if position[0] == posn[0] or position[1] == posn[1]:
            boardCopy.remove(posn)
    for i in range(1,n+1):
        if position[0] + i <= n:
            x1 = position[0] + i
        else:
            x1 = position[0]
        if position[0] - i >= 1:
            x2 = position[0] - i
        else:
            x2 = position[0]
        if position[1] +i <= n:
            y1 = position[1] +i
        else:
            y1 = position[1]
        if position[1] - i >= 1:
            y2 = position[1] -i
        else:
            y2 = position[1]
        try:
            if not([x1,y1] == position):
                boardCopy.remove([x1,y1])
        except:
            pass
        try:
            if not([x1,y2] == position):
                boardCopy.remove([x1,y2])
        except:
            pass
        try:
            if not([x2,y1] == position):
                boardCopy.remove([x2,y1])
        except:
            pass
        try:
            if not([x2,y2] == position):
                boardCopy.remove([x2,y2])
        except:
            pass
    return boardCopy

def getPositionList(board):
    '''
    this function takes the chess board as input
    returns the list of positions that are avaialable at the point.
    The list of positions means the places in 1st row that are remaining
    after removing the the overlapping positions or, positions that cannot
    be occupied.
    '''
    if len(board) == 0:
        return []
    c = board[0][0]
    posn = []
    for i in board:
        if i[0] == c:
            posn.append(i)
    return posn

def randomApproach(nQueen):
    board = makeBoard(nQueen)
    count = 0
    
    while True:
        boardCopy = board.copy()
        position = []
        for i in range(nQueen):
            try:
                posn = random.choice(getPositionList(boardCopy.copy()))
            except:
                continue
            position.append(posn)
            boardCopy = eliminateOverlaps(posn, boardCopy.copy() , nQueen)
        if len(position) == nQueen:
            return position
        elif count > 10000:
            break
        count +=1

if __name__ == "__main__":
    print(randomApproach(8))