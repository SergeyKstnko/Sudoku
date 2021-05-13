'''
This file contains backend of my Sudoky game
'''
import pdb


class Square:
    def __init__(self, val):
        self.val = val
        #if user can modify this square: 0 for no, 1 for yes.
        self.modifiable = 1 if val == 0 else 0
        self.text_color = 'dodgerblue2' if val ==0 else 'black'
        #self.modifiable = modifiable


def print_board(board):
    for r in range(9):
        if r%3 ==0 :
            print("\n------------------")
        print(end="|")
        for c in range(9):
            print(board[r][c].val, end="|")
        print("\n------------------")

    print()


def is_valid(board, ans, row, col):
    """
    This function checks if digit in certain square is valid
    
    param:      
    return: 1 for valid and 0 for not valid
    """
    for x in range(9):
        if board[row][x].val == ans and col != x:
            return 0
        elif board[x][col].val == ans and row != x:
            return 0
    
    for x in range(row//3*3, row//3*3+3):
        for y in range(col//3*3, col//3*3+3):
            if board[x][y].val == ans and x != row and y != col:
                return 0
    return 1


def is_solved(board):
    for r in range(9):
        for c in range(9):
            if not is_valid(board, board[r][c].val,r,c):
                #print("%d %d %d"% (board[r][c],r,c))
                return 0
    else: return 1


def solve(board,row,col):
    if row >= 9:
        return True
    else:
        #calculate next indecies for the next square
        next_col = (col+1)%9
        next_row = row
        if next_col == 0:
            next_row += 1


        if board[row][col].modifiable == 0:
            return solve(board,next_row,next_col)
        else:
            for val in range(1,10):

                if is_valid(board,val,row,col):
                    board[row][col].val = val
                    if solve(board,next_row,next_col):
                        return True
        board[row][col].val = 0
        return False


"""
Initial board
"""
board_int = [[6,0,5,0,0,0,1,0,0],
            [2,0,0,5,3,8,7,6,0],
            [0,3,0,0,6,2,0,0,0],
                
            [0,0,0,0,0,0,2,0,6],
            [0,5,0,0,0,6,3,0,9],
            [9,0,6,3,0,0,0,7,1],
                
            [0,0,7,0,5,4,0,8,3],
            [0,4,2,6,8,0,0,1,0],
            [0,6,0,9,0,3,4,0,7]]


board = [[Square(board_int[j][i]) for i in range(9)] for j in range(9)]

solve(board,0,0)

print_board(board)


"""
Initial board
"""
board_int = [[6,0,5,0,0,0,1,0,0],
            [2,0,0,5,3,8,7,6,0],
            [0,3,0,0,6,2,0,0,0],
                
            [0,0,0,0,0,0,2,0,6],
            [0,5,0,0,0,6,3,0,9],
            [9,0,6,3,0,0,0,7,1],
                
            [0,0,7,0,5,4,0,8,3],
            [0,4,2,6,8,0,0,1,0],
            [0,6,0,9,0,3,4,0,7]]


"""
solved board with 0 empty squares
"""
board_0 = [
        [6,8,5,4,7,9,1,3,2],
        [2,1,9,5,3,8,7,6,4],
        [7,3,4,1,6,2,5,9,8],

        [4,7,3,8,9,1,2,5,6],
        [8,5,1,7,2,6,3,4,9],
        [9,2,6,3,4,5,8,7,1],
        
        [1,9,7,2,5,4,6,8,3],
        [3,4,2,6,8,7,9,1,5],
        [5,6,8,9,1,3,4,2,7]
    ]

"""
board with only 1 empty square, the rest is solved correctly
"""
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