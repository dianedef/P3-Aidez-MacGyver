"""This module defines classes and functions related to the keeper'sprite in the game."""

import pygame

from constants import SPRITE_SIZE

from . import images


class KeeperSprite(pygame.sprite.Sprite):
    """This class represents the keeper's sprite on the screen."""

    def __init__(self, keeper, filename):
        """This function initializes a sprite from the superclass and from its
        file in the resources folder."""

        super().__init__()
        self.image, self.rect = images.load_image(filename, -1)
        self.keeper = keeper
        self.rect.x = self.keeper.position.x * SPRITE_SIZE
        self.rect.y = self.keeper.position.y * SPRITE_SIZE
