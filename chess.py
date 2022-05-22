#jdaniels
#26.03.2022
#chess game base

import pygame
import time
import random
import piece
import board

pygame.display.init()
screen = pygame.display.set_mode((800,600))

whpawnpath = "pieces/white_pawn.png"
#variables
done = False
img = pygame.image.load("board.png")
group = pygame.sprite.RenderPlain()
sel_piece = None
sel_check = False
x = y = 0
testpawn = piece.Piece((x, y), whpawnpath)    
group.add(testpawn)


def drawpieces():
    """draws some pieces"""    
    group.draw(screen)

def drawboard():
    """draws the background"""
    tempS = pygame.transform.scale(img, board.getsize())
    screen.blit(tempS, (400 - tempS.get_width()/2,\
                        300 - tempS.get_height()/2))


while not done:
    #erase
    screen.fill((0,0,0))
    pygame.event.pump()    
    
    #keyboard input
    PressedList = pygame.key.get_pressed()
    if PressedList[pygame.K_ESCAPE]:
        done = True   

    #mouse input
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and sel_piece is None:
            for p in group:
                if p.rect.collidepoint(pygame.mouse.get_pos()):
                    sel_piece = p
        elif event.type == pygame.MOUSEBUTTONUP and sel_piece:
            sel_piece.rect.topleft = board.grid[3][7]
            sel_piece = None
    print(pygame.mouse.get_pos())
    drawboard()
    drawpieces()
    pygame.display.flip()

pygame.display.quit()
