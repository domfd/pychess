from email.mime import image
import pygame


class Pawn(pygame.sprite.Sprite):

    def __init__(self, pos):
        super(Pawn, self).__init__()
        self.image = pygame.image.load("pieces/white_pawn.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        

    def update(self):
        pass