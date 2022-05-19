#jdaniels
#26.03.2022
#chess game base

import pygame
import time
import random
import piece

pygame.display.init()
screen = pygame.display.set_mode((800,600))

whpawnpath = "pieces/white_pawn.png"
#variables
done = False
img = pygame.image.load("board.png")
group = pygame.sprite.RenderPlain()
sel_piece = None
x = y = 150



def drawpieces():
    """draws some pieces"""
    testpawn = piece.Piece((x, y), whpawnpath)    
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
    
    #mouse input
    mousePressed = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    if mousePressed[0]:        
        if sel_piece == None:            
            for p in group:
                if p.rect.collidepoint(mousePos):
                    sel_piece = p
        else:
            sel_piece.rect.center(mousePos)
            sel_piece = None
    
    drawboard()
    drawpieces()
    pygame.display.flip()

pygame.display.quit()
