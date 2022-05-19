from email.mime import image
import pygame


class Piece(pygame.sprite.Sprite):

    def __init__(self, pos, path):
        super(Piece, self).__init__()
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        

    def update(self):
        pass