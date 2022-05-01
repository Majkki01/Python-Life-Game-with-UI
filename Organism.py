from random import random
import pygame
import random


class Organism:
    def __init__(self, x, y, world):
        self.x = x
        self.y = y
        world.add(self)
        self.alive = True
        self.age = 0

    def collision(self, attacker, world):
        if(self.strength > attacker.strength):
            world.Comments.append(type(attacker).__name__ + " attacks the " + type(self).__name__ + " and dies")
            attacker.alive = False
        else:
            world.Comments.append(type(attacker).__name__ + " attacks the " + type(self).__name__ + " and kills")
            self.alive = False