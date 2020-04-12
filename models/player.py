from copy import copy
import pygame

from models.position import Position
from models.item  import Item
from models.labyrinth import Labyrinth

class Player:    

    def __init__ (self, pseudo, bag, position, jeu):
        """ This function initialize a player with a name, an empty bag and a position"""
        self.pseudo = pseudo
        self.bag = bag
        self.position = position
        self.jeu = jeu

    def move(self, direction):
        """ The function sees if the direction chosen by the player is valid"""
        prev_position = copy(self.position)
        self.position.update(direction)
        if self.position in self.jeu.labyrinth.paths:
            #Voyons si nous sommes sur la case de sortie
            self.exit()
            # punch_sound = load_sound("punch.wav")
            # punch_sound.play() 
            # Voyons s'il y a un objet sur cette position
          #  self.catch_item()
            # whiff_sound = load_sound("whiff.wav")
            # whiff_sound.play() 
            # Faisons avancer MacGyver 
        else:
            self.position = prev_position
        self.catch_item()

    def catch_item(self):
        """ This function verifies if there is an object on the position of the caller, 
        changes its status and position, and delete it from the objects list """
        print("Well done, you got " + str(self.bag) + " object(s).")
        if self.position.xy in self.jeu.labyrinth.item_positions:
            self.bag += 1
            self.jeu.labyrinth.item_positions[self.position.xy].status = "catched"
            self.jeu.labyrinth.item_positions[self.position.xy].position = Position(self.bag, 15)
            del self.jeu.labyrinth.item_positions[self.position.xy]
        
    def exit(self):
        """ This function verifies if the caller is at the end of the labyrinth and if its bag is full, so that the game is lost or won"""
        print(self.jeu.labyrinth.end)
        print(self.position)
        if self.position == self.jeu.labyrinth.end:
            if self.bag == 3:
                print("Well done, you managed to put the keeper asleep and get out of the maze ! You won !")
                self.jeu.running = False
            else:
                print("Oops, there was still objects to catch... You lost !")
                self.jeu.running = False
        else:
            pass
