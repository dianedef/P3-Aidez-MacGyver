"""This module contains the graphical version of the game."""

import os
import random
import time
from copy import copy

import pygame
from pygame import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT

from constants import COLOR_GREEN, COLOR_MAROON, SPRITE_SIZE
from models.item import Item
from models.keeper import Keeper
from models.labyrinth import Labyrinth
from models.player import Player
from models.position import Position
from views.images import load_image
from views.items import ItemSprite
from views.keeper import KeeperSprite
from views.player import PlayerSprite


class Game:
    def __init__(self):
        """this function is called when the program starts.

        it initializes everything it needs, then runs in a loop until
        the function returns.
        """
        pygame.init()
        self.running = False
        self.labyrinth = Labyrinth()
        self.labyrinth.define_path("map.txt")
        self.player = Player(
            "MacGyver", 0, self.labyrinth.start.get_position(), self
        )
        self.keeper = Keeper(copy(self.labyrinth.end))
        self.tube = Item("Tube", self.labyrinth.random_pos(0))
        self.ether = Item("Ether", self.labyrinth.random_pos(1))
        self.needle = Item("Needle", self.labyrinth.random_pos(2))
        self.labyrinth.item_positions = {
            self.tube.position.xy: self.tube,
            self.ether.position.xy: self.ether,
            self.needle.position.xy: self.needle,
        }

    def start(self):
        """This function runs a windows for our game, creates our maze with
        paths and walls, a bar for the bag content to be shown."""

        self.running = True
        screen = pygame.display.set_mode(
            (
                self.labyrinth.width * SPRITE_SIZE,
                (self.labyrinth.length + 1) * SPRITE_SIZE,
            )
        )
        screen.fill(COLOR_GREEN)
        pygame.display.set_caption("Labyrinthe MacGyver")
        clock = pygame.time.Clock()

        background = pygame.Surface(
            (
                self.labyrinth.width * SPRITE_SIZE,
                self.labyrinth.length * SPRITE_SIZE,
            )
        )
        walls_image = pygame.image.load("resources/wall.png")
        for position in self.labyrinth.walls:
            background.blit(
                walls_image,
                (position.x * SPRITE_SIZE, position.y * SPRITE_SIZE),
            )
        path_image = pygame.image.load("resources/path.png")
        for position in self.labyrinth.paths:
            background.blit(
                path_image,
                (position.x * SPRITE_SIZE, position.y * SPRITE_SIZE),
            )

        # On ajoute les items
        # On instancie les sprite
        player_sprite = PlayerSprite(self.player, "player.png")
        keeper_sprite = KeeperSprite(self.keeper, "keeper.png")
        tube_sprite = ItemSprite(self.tube, "tube.png")
        ether_sprite = ItemSprite(self.ether, "ether.png")
        needle_sprite = ItemSprite(self.needle, "needle.png")

        allsprites = pygame.sprite.RenderPlain(
            player_sprite,
            needle_sprite,
            tube_sprite,
            keeper_sprite,
            ether_sprite,
        )

        while self.running:
            clock.tick(30)
            screen.blit(background, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.move("u")
                    elif event.key == pygame.K_DOWN:
                        self.player.move("d")
                    elif event.key == pygame.K_RIGHT:
                        self.player.move("r")
                    elif event.key == pygame.K_LEFT:
                        self.player.move("l")
                    else:
                        pass
                else:
                    pass

            # Draw Everything
            allsprites.update()
            allsprites.draw(screen)
            pygame.display.flip()


def main():
    jeu = Game()
    jeu.start()


if __name__ == "__main__":
    main()
