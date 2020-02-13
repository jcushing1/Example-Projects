#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 08:15:58 2019

#############################################
#Alpha-Beta Search for Generalized Tic-Tac-Toe
#############################################

import numpy as np

# self class is responsible for representing the game board
class GenGameBoard: 
    
    # Constructor method - initializes each position variable and the board size
    def __init__(self, boardSize):
        self.boardSize = boardSize  # Holds the size of the board
        self.marks = np.empty((boardSize, boardSize),dtype='str')  # Holds the mark for each position
        self.marks[:,:] = ' '
    
    # Prints the game board using current marks
    def printBoard(self): 
        # Print the column numbers
        print(' ',end='')
        for j in range(self.boardSize):
            print(" "+str(j+1), end='')
        
        
        # Print the rows with marks
        print("")
        for i in range(self.boardSize):
            # Print the line separating the row
            print(" ",end='')
            for j in range(self.boardSize):
                print("--",end='')
            
            print("-")

            # Print the row number
            print(i+1,end='')
            
            # Print the marks on self row
            for j in range(self.boardSize):
                print("|"+self.marks[i][j],end='')
            
            print("|")
                
        
        # Print the line separating the last row
        print(" ",end='')
        for j in range(self.boardSize):
            print("--",end='')
        
        print("-")
    
    
    # Attempts to make a move given the row,col and mark
    # If move cannot be made, returns False and prints a message if mark is 'X'
    # Otherwise, returns True
    def makeMove(self, row, col, mark):
        possible = False  # Variable to hold the return value
        if row==-1 and col==-1:
            return False
        
        # Change the row,col entries to array indexes
        row = row - 1
        col = col - 1
        
        if row<0 or row>=self.boardSize or col<0 or col>=self.boardSize:
            print("Not a valid row or column!")
            return False
        
        # Check row and col, and make sure space is empty
        # If empty, set the position to the mark and change possible to True
        if self.marks[row][col] == ' ':
            self.marks[row][col] = mark
            possible = True    
        
        # Print the message to the player if the move was not possible
        if not possible and mark=='X':
            print("\nself position is already taken!")
        
        return possible
    
    
    # Determines whether a game winning condition exists
    # If so, returns True, and False otherwise
    def checkWin(self, mark):
        won = False # Variable holding the return value
        # Check wins by examining each combination of positions
        
        # Check each row
        for i in range(self.boardSize):
            won = True
            for j in range(self.boardSize):
                if self.marks[i][j]!=mark:
                    won=False
                    break        
            if won:
                break

        # Check each column
        if not won:
            for i in range(self.boardSize):
                won = True
                for j in range(self.boardSize):
                    if self.marks[j][i]!=mark:
                        won=False
                        break
                if won:
                    break

        # Check first diagonal
        if not won:
            for i in range(self.boardSize):
                won = True
                if self.marks[i][i]!=mark:
                    won=False
                    break
                
        # Check second diagonal
        if not won:
            for i in range(self.boardSize):
                won = True
                if self.marks[self.boardSize-1-i][i]!=mark:
                    won=False
                    break

        return won
    
    # Determines whether the board is full
    # If full, returns True, and False otherwise
    def noMoreMoves(self):
        return (self.marks!=' ').all()

    def evaluation_function(self):
        
        score=0
        if (self.checkWin('X')):
            return -np.inf
        if (self.checkWin('O')):
            return np.inf

        # Check each row
        for i in range(self.boardSize):
            x=np.sum(board.marks[i,:]=='X')
            o=np.sum(board.marks[i,:]=='O')
            if (x==0):
                if (o>0):
                    score+=3**o
            if (o==0):
                if (x>0):
                    score-=3**x
             
        # Check each column
        for j in range(self.boardSize):
            x=np.sum(board.marks[:,j]=='X')
            o=np.sum(board.marks[:,j]=='O')
            if (x==0):
                if (o>0):
                    score+=3**o
            if (o==0):
                if (x>0):
                    score-=3**x
        
        diag1=board.marks.diagonal()
        diag2=np.fliplr(board.marks).diagonal()
        # Check first diagonal
        x=np.sum(diag1=='X')
        o=np.sum(diag1=='O')
        if (x==0):
            if (o>0):
                score+=3**o
        if (o==0):
            if (x>0):
                score-=3**x

        # Check second diagonal
        x=np.sum(diag2=='X')
        o=np.sum(diag2=='O')
        if (x==0):
            if (o>0):
                score+=3**o
        if (o==0):
            if (x>0):
                score-=3**x

        return score
    
    def makeCompMove(self):
    #computes the best move for the computer
        oldmarks=self.marks.copy()
        maxdepth=5  #depth for pruning
        best=None
        v=-np.inf #utility
        for (row,col) in [(i,j) for i in range(1,self.boardSize+1) for j in range(1,self.boardSize+1)]:
            if self.marks[row-1][col-1] != ' ':
                continue
            self.makeMove(row, col, 'O')
            vs=self.minvalue(maxdepth,-np.inf,np.inf)
            #print('{} {} {}'.format(row,col,vs))
            self.marks=oldmarks.copy()
            if (vs>v):
                v=vs
                best=(row,col)
        #print('alpha_beta_move: '+str(best)+' '+str(v))  #commented out to match format    
        (row,col)=best
        self.makeMove(row, col, 'O')
        return best

   
    def maxvalue(self,depth,alpha,beta):
    #computers the max value for minimax 
    #alpha is the guaranteed lower bound on the maximum value
    #beta is the guaranteed upper bound on the minimum value
        s=self.evaluation_function()
        if (depth<=0) or (s==np.inf) or (s==-np.inf) or np.sum(board.marks==' ')==0:
            return s
        v=-np.inf
        oldmarks=self.marks.copy()
        for (row,col) in [(i,j) for i in range(1,self.boardSize+1) for j in range(1,self.boardSize+1)]:
            if self.marks[row-1][col-1] != ' ':
                continue
            self.makeMove(row, col, 'O')
            vs=self.minvalue(depth-1,alpha,beta)           
            #print('max: {} {} {}'.format(row,col,vs))
            self.marks=oldmarks.copy()
            v=max(v,vs)
            alpha=max(alpha,v)
            if (alpha>=beta):
                break
        return v       
    
    def minvalue(self,depth,alpha,beta):
    #computes the min value for minimax
        s=self.evaluation_function()
        if (depth<=0) or (s==np.inf) or (s==-np.inf) or np.sum(board.marks==' ')==0:
            return s
        v=np.inf
        oldmarks=self.marks.copy()
        for (row,col) in [(i,j) for i in range(1,self.boardSize+1) for j in range(1,self.boardSize+1)]:
            if self.marks[row-1][col-1] != ' ':
                continue
            self.makeMove(row, col, 'X')
            vs=self.maxvalue(depth-1,alpha,beta)  
            #print('min: {} {} {}'.format(row,col,vs))
            self.marks=oldmarks.copy()
            v=min(v,vs)
            beta=min(beta,v)
            if (beta<=alpha):
                break
        return v       
        
        

LOST = 0
WON = 1
DRAW = 2    
wrongInput = False
boardSize = int(input("Please enter the size of the board n (e.g. n=3,4,5,...): "))
        
# Create the game board of the given size
board = GenGameBoard(boardSize)
        
board.printBoard()  # Print the board before starting the game loop
        
# Game loop
while True:
    # *** Player's move ***        
    
    # Try to make the move and check if it was possible
    # If not possible get col,row inputs from player    
    row, col = -1, -1
    while not board.makeMove(row, col, 'X'):
        print("Player's Move")
        row, col = input("Choose your move (row, column): ").split(',')
        row = int(row)
        col = int(col)

    # Display the board again
    board.printBoard()
            
    # Check for ending condition
    # If game is over, check if player won and end the game
    if board.checkWin('X'):
        # Player won
        result = WON
        break
    elif board.noMoreMoves():
        # No moves left -> draw
        result = DRAW
        break
            
    # *** Computer's move ***
    board.makeCompMove()
    
    # Print out the board again
    board.printBoard()    
    
    # Check for ending condition
    # If game is over, check if computer won and end the game
    if board.checkWin('O'):
        # Computer won
        result = LOST
        break
    elif board.noMoreMoves():
        # No moves left -> draw
        result = DRAW
        break
        
# Check the game result and print out the appropriate message
print("GAME OVER")
if result==WON:
    print("You Won!")            
elif result==LOST:
    print("You Lost!")
else: 
    print("It was a draw!")
