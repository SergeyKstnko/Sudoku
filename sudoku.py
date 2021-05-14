'''
This file is the game itself and front-end of Sudoky game
'''

import pygame
import sys
import math
import backend as be
from pygame_widgets import Button

WINDOW_WIDTH = 440
WINDOW_HEIGHT = 450
lrg_rect_width = WINDOW_WIDTH/3
lrg_rect_height = WINDOW_HEIGHT/3
sm_rect_width = WINDOW_WIDTH/9
sm_rect_height = WINDOW_HEIGHT/9
game_running = True

clicked_row = -1
clicked_col = -1


pygame.init()

#create game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT+50))


#set title
pygame.display.set_caption("Weeeelcome the one and only Sudoky game.")

board = [[be.Square(be.board_int[j][i]) for i in range(9)] for j in range(9)]


#main game loop
while game_running:
    #color of the background
    game_window.fill((210,255,255))    
    font = pygame.font.Font(None, 32)

    #game content
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            

            if clicked_col in range(9) and clicked_row in range(9):
                board[clicked_row][clicked_col].frame_color = (0,0,0)
                board[clicked_row][clicked_col].frame_thickness = be.Square.unclicked_thickness

            clicked_row = int(event.pos[1] // sm_rect_height)
            clicked_col = int(event.pos[0] // sm_rect_height)

            if clicked_col in range(9) and clicked_row in range(9):

                if board[clicked_row][clicked_col].modifiable == 1:
                    board[clicked_row][clicked_col].frame_color = (255,0,0)
                    board[clicked_row][clicked_col].frame_thickness = be.Square.clicked_thickness

                elif board[clicked_row][clicked_col].modifiable == 0:
                    clicked_row = -1 
                    clicked_col = -1
                
            if clicked_col <9 and clicked_row < 9:
                print("(%d,%d) value: %d"% (clicked_col, clicked_row, board[clicked_row][clicked_col].val))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                be.print_board(board)
            elif event.key == pygame.K_SPACE:
                be.solve_board(board, game_window)
            if clicked_col >= 0 and clicked_row >=0:
                if event.key == pygame.K_RETURN:
                    board[clicked_row][clicked_col].frame_color = (0,0,0)
                    board[clicked_row][clicked_col].frame_thickness = be.Square.unclicked_thickness
                    clicked_row = -1
                    clicked_col = -1
                    print("Zeroed out (%d,%d)"% (clicked_col, clicked_row))
                elif event.key == pygame.K_BACKSPACE:
                    print("BACKSPACE was pressed")
                    board[clicked_row][clicked_col].val = 0
                elif event.key >= pygame.K_0 and event.key <= pygame.K_9:
                    board[clicked_row][clicked_col].val = 0
                    board[clicked_row][clicked_col].val += int(event.unicode)

    
    be.update_screen(board, game_window)       


    
pygame.quit()
sys.exit()