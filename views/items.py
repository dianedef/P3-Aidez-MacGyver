from .images import load_image
from constants import SPRITE_SIZE

import pygame

class ItemSprite(pygame.sprite.Sprite): 
    """yy"""
    def __init__(self, item, filename):
        super().__init__()        #Appel du constructeur de Sprite
        self.image, self.rect = load_image(filename, -1)
        self.item = item

    def update(self):
        "hh"
        self.rect.x = self.item.position.x * SPRITE_SIZE
        self.rect.y = self.item.position.y * SPRITE_SIZE