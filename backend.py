'''
This file contains backend of my Sudoky game
'''

class Square:
    def __init__(self, value, modifiable):
        self.value = value
        #can user modify this square: 0 for no 1 for yes.
        self.modifiable = modifiable

    def change_value(value):
        self.value = value



def print_board():
    print()
    for r in range(9):
        print(end="|")
        for c in range(9):
            print(board[r][c], end="|")
        print("\n------------------")
    print()

def is_valid(board, ans, row, col):
    for x in range(9):
        if board[row][x] == ans and col != x:
            return 0
        elif board[x][col] == ans and row != x:
            return 0
    
    for x in range(row//3*3, row//3*3+3):
        for y in range(col//3*3, col//3*3+3):
            if board[x][y] == ans and x != row and y != col:
                return 0
    return 1

def is_solved(board):
    for r in range(9):
        for c in range(9):
            if not is_valid(board, board[r][c],r,c):
                #print("%d %d %d"% (board[r][c],r,c))
                return 0
    else: return 1

#def initialize(board):



board = [[6,0,5,0,0,0,1,0,0],
        [2,0,0,5,3,8,7,6,0],
        [0,3,0,0,6,2,0,0,0],
            
        [0,0,0,0,0,0,2,0,6],
        [0,5,0,0,0,6,3,0,9],
        [9,0,6,3,0,0,0,7,1],
            
        [0,0,7,0,5,4,0,8,3],
        [0,4,2,6,8,0,0,1,0],
        [0,6,0,9,0,3,4,0,7]]

board_0 = [
        [1,8,5,4,7,9,1,3,2],
        [2,1,9,5,3,8,7,6,4],
        [7,3,4,1,6,2,5,9,8],

        [4,7,3,8,9,1,2,5,6],
        [8,5,1,7,2,6,3,4,9],
        [9,2,6,3,4,5,8,7,1],
        
        [1,9,7,2,5,4,6,8,3],
        [3,4,2,6,8,7,9,1,5],
        [5,6,8,9,1,3,4,2,7]
    ]

board_1 = [
        [0,8,5,4,7,9,1,3,2],
        [2,1,9,5,3,8,7,6,4],
        [7,3,4,1,6,2,5,9,8],

        [4,7,3,8,9,1,2,5,6],
        [8,5,1,7,2,6,3,4,9],
        [9,2,6,3,4,5,8,7,1],
        
        [1,9,7,2,5,4,6,8,3],
        [3,4,2,6,8,7,9,1,5],
        [5,6,8,9,1,3,4,2,7]
    ]