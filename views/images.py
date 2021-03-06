"""This module defines the function that loads the sprite images in te graphical game."""

import os

import pygame


def load_image(name, colorkey=None):
    """This function tries to load an image from the folder 'resources", size
    it and returns it with a rect.

    Otherwise returns an error message.
    """

    fullname = os.path.join('resources', name)
    try:
        image = pygame.transform.scale(pygame.image.load(fullname), (50, 50))
    except pygame.error:
        print("Cannot load image :", name)
        raise SystemExit
    image = image.convert_alpha()
    return image, image.get_rect()
