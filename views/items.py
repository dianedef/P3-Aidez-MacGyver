"""This module defines classes and functions related to the items'sprites in the game."""

import pygame

from constants import SPRITE_SIZE

from .images import load_image


class ItemSprite(pygame.sprite.Sprite):
    """This class represents the item's sprites on the screen."""

    def __init__(self, item, filename):
        """This function initializes a sprite from the superclass and from its
        file in the resources folder."""
        super().__init__()  # Appel du constructeur de Sprite
        self.image, self.rect = load_image(filename, -1)
        self.item = item

    def update(self):
        """This function updates the rect of the item from its position to fit
        the screen size."""
        self.rect.x = self.item.position.x * SPRITE_SIZE
        self.rect.y = self.item.position.y * SPRITE_SIZE
