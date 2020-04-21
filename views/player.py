"""This module defines classes and functions related to the player'sprite in the game."""

import pygame

from constants import SPRITE_SIZE

from .images import load_image


class PlayerSprite(pygame.sprite.Sprite):
    """This class represents the player's sprite on the screen."""

    def __init__(self, player, filename):
        """This function initializes a sprite from the superclass and from its
        file in the resources folder."""

        super().__init__()
        self.image, self.rect = load_image(filename, -1)
        self.player = player
        self.bag = 0

    def update(self):
        """This function moves the player sprite according to the player
        position."""

        self.rect.x = self.player.position.x * SPRITE_SIZE
        self.rect.y = self.player.position.y * SPRITE_SIZE
