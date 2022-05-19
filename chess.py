#jdaniels
#26.03.2022
#chess game base

import pygame
import time
import random
import Piece

pygame.display.init()
screen = pygame.display.set_mode((800,600))

#variables
done = False
img = pygame.image.load("board.png")
group = pygame.sprite.RenderPlain()
events = pygame.event.get()

x = y = 150



def drawpieces():
    """draws some pieces"""
    testpawn = Piece.Pawn((x, y))    
    group.add(testpawn)
    group.draw(screen)

def drawboard():
    """draws the background"""
    owd = img.get_width() 
    oht = img.get_height() 
    newwid = int(owd*1)
    newhie = int(oht*1)
    tempS = pygame.transform.scale(img, (newwid, newhie))
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
    
    #check for mouseclick => find selected piece
    # NOT TESTED
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for piece in group:
                if piece.rect.collidepoint(pos):
                    sel_piece = piece
                    
   
    drawboard()
    drawpieces()
    pygame.display.flip()

pygame.display.quit()
