'''
This file is the game itself and front-end of Sudoky game
'''

import pygame
import sys
import backend as be

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
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


#set title
pygame.display.set_caption("Weeeelcome the one and only Sudoky game.")

board = [[be.Square(be.board_int[j][i]) for i in range(9)] for j in range(9)]

#main game loop
while game_running:
    is_full = 0
    #color of the background
    game_window.fill((210,255,255))    
    font = pygame.font.Font(None, 32)

    #game content
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // sm_rect_height)
            clicked_col = int(mouseX // sm_rect_height)

            if board[clicked_row][clicked_col].modifiable == 0:
                clicked_row = -1 
                clicked_col = -1

            print("(%d,%d) value: %d"% (clicked_col, clicked_row, board[clicked_row][clicked_col].val))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                be.print_board()
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

    
    for r in range(9):
        for c in range(9):
            #draw large rectangle if it is time
            if r%3 == 0 and c%3 == 0:
                lrg_rect = pygame.Rect(c/3*lrg_rect_width, r/3*lrg_rect_height, lrg_rect_width, lrg_rect_height)
                pygame.draw.rect(game_window, (0,0,0), lrg_rect, 4)
                #draw small rectangle   
                # (from left, from top, width, height)
            
            sm_rect = pygame.Rect(c*sm_rect_width, r*sm_rect_height, sm_rect_width, sm_rect_height)
                #(where, color, what to draw)
            if r == clicked_row and c == clicked_col:
                color = (255,0,0)
                border = 4
            else:
                color = (0,0,0)
                border = 2
            pygame.draw.rect(game_window, color, sm_rect, border)

            #draw number
                #Render text
            if board[r][c].val > 0:
                txt_surface = font.render(str(board[r][c].val), True, pygame.Color(board[r][c].text_color)) 
                game_window.blit(txt_surface, (c*sm_rect_width+17, r*sm_rect_height+15))
            if board[r][c].val == 0:
                is_full += 1

    if is_full == 0 and be.is_solved(board):

        print("YOOOOOOUUU SOOOOOOOOOLVED ITTTTT")
        game_running = False
    
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