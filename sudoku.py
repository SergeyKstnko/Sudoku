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

'''
button = Button(
            game_window, 15, WINDOW_HEIGHT+8, 125, 35, text='Solve',
            fontSize=50, margin=20,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: print('Click')
         )
'''

#main game loop
while game_running:
    #is_full = 0
    #color of the background
    game_window.fill((210,255,255))    
    font = pygame.font.Font(None, 32)

    #game content
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            clicked_row = int(event.pos[1] // sm_rect_height)
            clicked_col = int(event.pos[0] // sm_rect_height)

            if clicked_col <9 and clicked_row < 9 and board[clicked_row][clicked_col].modifiable == 0:
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
                    clicked_row = -1
                    clicked_col = -1
                    print("Zeroed out (%d,%d)"% (clicked_col, clicked_row))
                elif event.key == pygame.K_BACKSPACE:
                    print("BACKSPACE was pressed")
                    board[clicked_row][clicked_col].val = 0
                elif event.key >= pygame.K_0 and event.key <= pygame.K_9:
                    board[clicked_row][clicked_col].val = 0
                    board[clicked_row][clicked_col].val += int(event.unicode)
            

    #button.listen(event)
    #button.draw()

    
    be.update_screen(board, game_window)       

    
    #pygame.display.update()
    #pygame.event.pump()
    pygame.display.flip()


    #pygame.draw.line(game_window, (255,0,0), (100, 100), (300, 200), 5)

    #empty_rect = pygame.Rect(400, 200, 25, 25)
    #pygame.draw.rect(game_window, (255,0,0), empty_rect, 0)

    #points = [(150, 150), (200, 120), (210, 150), (260, 140), (210, 250)]
    #pygame.draw.polygon(game_window, (0,0,0), points)

    
pygame.quit()
sys.exit()