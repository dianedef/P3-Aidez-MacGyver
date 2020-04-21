"""This module contains the terminal version of the game."""

import random
from copy import copy

from models.item import Item
from models.keeper import Keeper
from models.labyrinth import Labyrinth
from models.player import Player
from models.position import Position


class Game:
    def __init__(self):
        """This function initialize the game with a labyrinth, a player, a
        keeper, and 3 items at random positions on the labyrinth."""

        self.running = False
        self.labyrinth = Labyrinth()
        self.labyrinth.define_path("map.txt")
        self.player = Player("MacGyver", 0, copy(self.labyrinth._start))
        self.garde = Keeper(self.labyrinth._end)
        self.items_positions = self.labyrinth.random_pos()
        self.items = [
            Item("a needle", self.items_positions[0]),
            Item("a plastic tube", self.items_positions[1]),
            Item("ether", self.items_positions[2]),
        ]

    def exit(self):
        """This function checks if the bag of the player is full."""

        if self.player.bag == 3:
            print(
                "Well done, you managed to put the keeper asleep and get out of the maze ! You won !"
            )
        else:
            print("Oops, there was still objects to catch... You lost !")

    def start(self):
        """This function starts the game, moves the player to a direction
        inputed if authorized, calls the exit function, catches items."""

        self.running = True
        while self.running:
            initial_position = copy(self.player.position)
            print("\nYour position is : " + str(initial_position))
            direction = str(
                input("Where do you want to go ? \n Type 'u' 'd' 'l' ou 'r' ")
            )
            self.player.position.update(direction)
            print("Objects are here : " + str(self.items_positions))

            if self.player.position == Position(14, 14):
                self.exit()
            else:
                if self.player.position in self.items_positions:
                    self.player.bag += 1
                    print(
                        "Well done, you go "
                        + str(self.player.bag)
                        + " object(s)."
                    )
                else:
                    pass
                if self.player.position in self.labyrinth._paths:
                    print("\nYou're one step ahead !")
                else:
                    print("\nThis step is forbidden !")
                    self.player.position = initial_position
                print("Your position is now : " + str(self.player.position))


def main():
    jeu = Game()
    jeu.start()


if __name__ == "__main__":
    main()
