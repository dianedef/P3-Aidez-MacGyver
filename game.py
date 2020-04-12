from models.item import Item
from models.position import Position
from models.player import Player
from models.keeper import Keeper
from models.labyrinth import Labyrinth

import random
from copy import copy

class Game:
    def __init__(self):
        """ This function initialize the game with a labyrinth, a player, a keeper, and 3 items at random positions on the labyrinth"""
        self.running = False
        self.labyrinth = Labyrinth()
        self.labyrinth.define_path("map.txt")
        self.player = Player("MacGyver", 0, copy(self.labyrinth._start))
        self.garde = Garde(self.labyrinth._end)
        self.items_positions = self.labyrinth.random_pos()
        self.items = [
            Item("une aiguille", self.items_positions[0]), 
            Item("un petit tube en plastique", self.items_positions[1]), 
            Item("de l'éther", self.items_positions[2])
        ] 

    def exit(self):
        """ This function checks if the bag of the player is full"""
        if self.player.bag == 3:
            print("Bravo, vous avez pu endormir le garde et sortir du labyrinthe, vous avez gagné !")
        else:
            print("Et non, il vous manquait un ou des objets, perdu")

    def start(self):
        self.running = True
        while self.running: 
            position_initiale = copy(self.player.position)
            print( "\nVotre position est : " + str(position_initiale))
            direction = str(input("Où voulez-vous aller ? \n Tapez 'u' 'd' 'l' ou 'r' "))
            self.player.position.update(direction)            
            print("Les objets sont ici : "+ str(self.items_positions))

            #Voyons si nous sommes sur la case de sortie
            if self.player.position == Position(14, 14):
                self.exit()
            else:
                # Voyons s'il y a un objet sur cette position
                if self.player.position in self.items_positions:
                    self.player.bag += 1
                    print("Bravo, vous avez " + str(self.player.bag) + " objet(s).")
                else:
                    pass

                # Voyons si la direction invite à une position valide
                if self.player.position in self.labyrinth._paths:
                    print("\nVous avez avancé d'une case !")
                else:
                    print("\nCe chemin n'est pas autorisé !")
                    self.player.position = position_initiale
                print("Votre position est maintenant : " + str(self.player.position))

def main():
    jeu = Game()
    jeu.start()

if __name__ == '__main__':
    main()