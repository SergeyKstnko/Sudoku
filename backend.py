'''
This file contains support functions that process the information that was collected
from a user by the sudoku.py and display it on the window.

@author Sergey Kostenko
@version 05/14/21
'''

import pygame

WINDOW_WIDTH = 440
WINDOW_HEIGHT = 450
lrg_rect_width = WINDOW_WIDTH/3
lrg_rect_height = WINDOW_HEIGHT/3
sm_rect_width = WINDOW_WIDTH/9
sm_rect_height = WINDOW_HEIGHT/9

class Square:
    #thickness of the square frame
    clicked_thickness = 3
    unclicked_thickness = 1

    def __init__(self, val):
        self.val = val
        #if user can modify this square: 0 for no, 1 for yes.
        self.modifiable = 1 if val == 0 else 0
        self.text_color = 'dodgerblue2' if val ==0 else 'black'
        self.frame_color = (0,0,0)
        self.frame_thickness = Square.unclicked_thickness


def print_board(board):
    """
    This function prints board in terminal
    :param      board: 2D array of objects Square
    :return:    none
    """
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
    This function checks the validity of a digit in certain square according to
    rules of Sudoku
    
    :param:     board: 2D array of objects Square
                ans: digit that is being places in that position
                row: row where the digit is located
                col: column where the digit is located
    :return:    1 for valid and 0 for not valid
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
    """
    This function checks if the board is solved
    
    :param:     board: 2D array of objects Square
    :return:    1 if board is solved and 0 if board was not solved
    """
    for r in range(9):
        for c in range(9):
            if not is_valid(board, board[r][c].val,r,c):
                return 0
    else: return 1


def update_screen(board, game_window):
    """
    This function refreshes and draws the board, timer and a message in
    the bottom left corner on the game window
    
    :param:     board: 2D array of objects Square
                game_window: game window the board is drawn
    :return:    none
    """
    is_full = 0
    font = pygame.font.Font(None, 32)
    game_window.fill((210,255,255)) 
    for r in range(9):
        for c in range(9):
            
            #draw large rectangle if it is time
            if r%3 == 0 and c%3 == 0:
                lrg_rect = pygame.Rect(c/3*lrg_rect_width, r/3*lrg_rect_height, lrg_rect_width, lrg_rect_height)
                pygame.draw.rect(game_window, (0,0,0), lrg_rect, 4)

            #draw small rectangle   
                # (from left, from top, width, height)
            sm_rect = pygame.Rect(c*sm_rect_width, r*sm_rect_height, sm_rect_width+1, sm_rect_height)
                #(where, color, what to draw)
            pygame.draw.rect(game_window, board[r][c].frame_color, sm_rect, board[r][c].frame_thickness)
            
            #draw number
                #Render text
            if board[r][c].val > 0:
                txt_surface = font.render(str(board[r][c].val), True, pygame.Color(board[r][c].text_color)) 
                game_window.blit(txt_surface, (c*sm_rect_width+17, r*sm_rect_height+15))
            
            if board[r][c].val == 0:
                is_full += 1


    sec =  pygame.time.get_ticks() / 1000
    min = sec // 60
    hour = min // 60

    timer = "%02d:%02d:%02d" % (hour%24, min%60, sec%60)
    txt_surface = font.render(timer, True, pygame.Color('grey'))
    game_window.blit(txt_surface, (WINDOW_WIDTH-105, WINDOW_HEIGHT+15))  
    
    if is_full == 0 and is_solved(board):
        text = "Congrats!! It is solved"
        color = 'red'
    else:
        text = "Press SPACE to solve"
        color = 'grey'

    txt_surface = font.render(text, True, pygame.Color(color))
    game_window.blit(txt_surface, (10, WINDOW_HEIGHT+15))

    pygame.display.flip()



def solve(board,row,col, game_window):    
    """
    This recursive function tries to fit digits 1 to 9 into the square
    and see if it is valid or not. This functions helps implement 
    backtracking algorithm that allows computer to solve the board for 
    the user
    
    :param:     board: 2D array of objects Square
                row: row where to try fit digits
                col: column where to try fit digits
    :return:    True: if the board is solved
                False: if no digits between 1 and 9 are valid for this square
    """
    if row >= 9:
        return True
    else:
        #calculate next indecies for the next square
        next_col = (col+1)%9
        next_row = row
        if next_col == 0:
            next_row += 1


        if board[row][col].modifiable == 0:
            if not is_valid(board,board[row][col].val,row,col):
                return False
            return solve(board,next_row,next_col, game_window)
        else:
            for val in range(1,10):

                if is_valid(board,val,row,col):
                    
                    board[row][col].val = val
                    board[row][col].frame_color = (0,255,0)
                    board[row][col].frame_thickness = Square.clicked_thickness

                    pygame.time.wait(100)
                    update_screen(board, game_window)
                    

                    if solve(board,next_row,next_col, game_window):
                        return True
        board[row][col].val = 0
        board[row][col].frame_color = (255,0,0)

        return False


def solve_board(board, game_window):
    """
    This function prepares the board for the use of backtracking algorithm
    by resetting all squares that were ment to be filled by the user to 0.
    After backtracking algorithm is done this function unsellects all the
    squares.
    :param:     board: 2D array of objects Square
                game window: game window where the board is drawn
    :return:    none
    """
    #reset all squares that were ment to be filled up by the user to 0
    for r in range(9):
        for c in range(9):
            if board[r][c].modifiable == 1:
                board[r][c].val = 0
                board[r][c].frame_color = (0,0,0)
                board[r][c].frame_thickness = Square.unclicked_thickness

    if solve(board,0,0,game_window) == False:
        print("This board has no solution")

    #unselects all squares
    for r in range(9):
        for c in range(9):
            board[r][c].frame_color = (0,0,0)
            board[r][c].frame_thickness = Square.unclicked_thickness


#Below are examples of different boards.
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