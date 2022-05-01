import random
import numpy
from Organism import Organism
from constants import BELLADONNA, GRASS, GUARANA, HOGWEED, SOW_THISTLE
from Animal import Animal, CyberSheep

class Plant(Organism):
    def __init__(self,x,y,world):
        self.initiative = 0
        super().__init__(x, y, world)

    def action(self, world):
        NEIGHBOURS = [0,0,0,0]

        for i in world.Organisms:
            if(i.x == self.x + 1 and i.y == self.y and type(i) == type(self)):
                    NEIGHBOURS[0] = 1
            if(i.x == self.x - 1 and i.y == self.y and type(i) == type(self)):
                    NEIGHBOURS[1] = 1
            if(i.x == self.x and i.y == self.y + 1 and type(i) == type(self)):
                    NEIGHBOURS[2] = 1
            if(i.x == self.x and i.y == self.y - 1 and type(i) == type(self)):
                    NEIGHBOURS[3] = 1

        rand1 = random.randint(1,4)
        rand2 = random.randint(0,99)

        if(rand2 < 10):
            if((rand1 == 1 and self.x < 19) or (rand1 == 2 and self.x == 0)):
                if(NEIGHBOURS[0] == 0):
                    (type(self)(self.x + 1, self.y, world))
                    world.Comments.append(type(self).__name__ + " is spreading")
            elif(rand1 == 2 or rand1 == 1 ):
                if(NEIGHBOURS[1] == 0):
                    (type(self)(self.x - 1, self.y, world))
                    world.Comments.append(type(self).__name__ + " is spreading")
            elif((rand1 == 3 and self.y < 19) or (rand1 == 4 and self.y == 0)):
                if(NEIGHBOURS[2] == 0):
                    (type(self)(self.x, self.y + 1, world))
                    world.Comments.append(type(self).__name__ + " is spreading")
            elif(rand1 == 4 or rand1 == 3):
                if(NEIGHBOURS[3] == 0):
                    (type(self)(self.x, self.y - 1, world))
                    world.Comments.append(type(self).__name__ + " is spreading")


class Grass(Plant):
    def __init__(self, x, y, world):
        self.image = GRASS
        self.strength = 0
        super().__init__(x, y, world)

class SowThistle(Plant):
    def __init__(self, x, y, world):
        self.image = SOW_THISTLE
        self.strength = 0
        super().__init__(x, y, world)

    def action(self, world):
        i=0
        while i < 3:
            super().action(world)
            i = i + 1

class Guarana(Plant):
    def __init__(self, x, y, world):
        self.image = GUARANA
        self.strength = 0
        super().__init__(x, y, world)

    def collision(self, attacker, world):
        if(issubclass(type(attacker), Animal)):
            world.Comments.append("Guarana increases the strength of " + type(attacker).__name__)
            attacker.strength = attacker.strength + 3

        super().collision(attacker, world)

class Belladonna(Plant):
    def __init__(self, x, y, world):
        self.image = BELLADONNA
        self.strength = 99
        super().__init__(x, y, world)

    def collision(self, attacker, world):
        if(issubclass(type(attacker), Animal)):
            world.Comments.append(type(attacker).__name__ + " eats Belladonna and dies")
            self.alive = False
            attacker.alive = False
        else:
            super().collision(attacker, world)

class SosnowskysHogweed(Plant):
    def __init__(self, x, y, world):
        self.image = HOGWEED
        self.strength = 10
        super().__init__(x, y, world)

    def action(self, world):
        for i in world.Organisms:
            if(((i.x == self.x and (i.y == self.y + 1 or i.y == self.y - 1)) or (i.y == self.y and (i.x == self.x + 1 or i.x == self.x - 1))) and type(i) != CyberSheep):
                world.Comments.append(type(i).__name__ + " steps to close to Hogweed and dies")
                i.alive = False

    def collision(self, attacker, world):
        if(issubclass(type(attacker), Animal) and type(attacker) != CyberSheep):
            world.Comments.append(type(attacker).__name__ + " eats Hogweed and dies")
            self.alive = False
            attacker.alive = False
        else:
            super().collision(attacker, world)