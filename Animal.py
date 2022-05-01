import random
from Organism import Organism
from constants import ANTELOPE, CYBERSHEEP, HOGWEED, HUMAN, WOLF, SHEEP, FOX, TURTLE

class Animal(Organism):
    def __init__(self, x, y, world):
        if(x != 0): self.prev_x = x - 1
        else: self.prev_x = x + 1
        self.prev_y = y
        self.breeding_delay = 0
        super().__init__(x, y, world)

    def action(self, world):
        self.prev_x = self.x
        self.prev_y = self.y
        self.breeding_delay = self.breeding_delay + 1

        rand = random.randint(1,4)
        if((rand == 1 and self.x < 19) or (rand == 2 and self.x == 0)):
            self.x+=1
        elif(rand == 2 or rand == 1 ):
            self.x-=1
        elif((rand == 3 and self.y < 19) or (rand == 4 and self.y == 0)):
            self.y+=1
        elif(rand == 4 or rand == 3):
            self.y-=1

    def reverse_action(self):
        self.x = self.prev_x
        self.y = self.prev_y


class Wolf(Animal):
    def __init__(self, x, y, world):
        self.image = WOLF
        self.initiative = 5
        self.strength = 9
        super().__init__(x, y, world)


class Sheep(Animal):
    def __init__(self, x, y, world):
        self.image = SHEEP
        self.initiative = 4
        self.strength = 4
        super().__init__(x, y, world)


class Fox(Animal):
    def __init__(self, x, y, world):
        self.image = FOX
        self.initiative = 7
        self.strength = 3
        super().__init__(x, y, world)

    def action(self, world):
        self.prev_x = self.x
        self.prev_y = self.y
        self.breeding_delay = self.breeding_delay + 1

        rand = random.randint(1,4)

        NEIGHBOURS = [0,0,0,0]

        for i in world.Organisms:
            if(i.x == self.x + 1 and i.y == self.y and i.strength > self.strength):
                    NEIGHBOURS[0] = 1
            if(i.x == self.x - 1 and i.y == self.y and i.strength > self.strength):
                    NEIGHBOURS[1] = 1
            if(i.x == self.x and i.y == self.y + 1 and i.strength > self.strength):
                    NEIGHBOURS[2] = 1
            if(i.x == self.x and i.y == self.y - 1 and i.strength > self.strength):
                    NEIGHBOURS[3] = 1

        counter = 0
        while counter < 2:
            if((rand == 1 and NEIGHBOURS[0] == 1) or self.x == 19):
                rand = 2
            if((rand == 2 and NEIGHBOURS[1] == 1) or self.x == 0):
                rand = 3
            if((rand == 3 and NEIGHBOURS[2] == 1) or self.y == 19):
                rand = 4
            if((rand == 4 and NEIGHBOURS[3] == 1) or self.y == 0):
                rand = 1
            
            counter = counter + 1

        if((rand == 1 and self.x < 19) or (rand == 2 and self.x == 0)):
            self.x+=1
        elif(rand == 2 or rand == 1 ):
            self.x-=1
        elif((rand == 3 and self.y < 19) or (rand == 4 and self.y == 0)):
            self.y+=1
        elif(rand == 4 or rand == 3):
            self.y-=1

class Turtle(Animal):
    def __init__(self, x, y, world):
        self.image = TURTLE
        self.initiative = 1
        self.strength = 2
        super().__init__(x, y, world)

    def action(self, world):
        rand = random.randint(0,99)

        if(rand < 25):
            super().action(world)

    def collision(self, attacker, world):
        if(attacker.strength < 5 and issubclass(type(attacker), Animal)):
            world.Comments.append("Turtle refelcts " + type(attacker).__name__ + "'s attack")
            attacker.reverse_action()
        else:
            super().collision(attacker, world)

class Antelope(Animal):
    def __init__(self, x, y, world):
        self.image = ANTELOPE
        self.initiative = 4
        self.strength = 4
        super().__init__(x, y, world)

    def action(self, world):
        self.prev_x = self.x
        self.prev_y = self.y
        self.breeding_delay = self.breeding_delay + 1

        rand = random.randint(1,4)
        if((rand == 1 and self.x < 18) or (rand == 2 and self.x < 2)):
            self.x+=2
        elif(rand == 2 or rand == 1 ):
            self.x-=2
        elif((rand == 3 and self.y < 18) or (rand == 4 and self.y < 2)):
            self.y+=2
        elif(rand == 4 or rand == 3):
            self.y-=2

    def collision(self, attacker, world):
        escape = random.randint(0,1)
        if(attacker.strength >= self.strength and escape == 1):
            world.Comments.append("Antelope manages to escape the fight")
            NEIGHBOURS = [0,0,0,0]

            if(self.x == 19): NEIGHBOURS[0] = -1
            elif(self.x == 0): NEIGHBOURS[1] = -1

            if(self.y == 19): NEIGHBOURS[2] = -1
            elif(self.y == 0): NEIGHBOURS[3] = -1

            for i in world.Organisms:
                if(i.x == self.x + 1 and i.y == self.y):
                        NEIGHBOURS[0] = 1
                if(i.x == self.x - 1 and i.y == self.y):
                        NEIGHBOURS[1] = 1
                if(i.x == self.x and i.y == self.y + 1):
                        NEIGHBOURS[2] = 1
                if(i.x == self.x and i.y == self.y - 1):
                        NEIGHBOURS[3] = 1

            if(NEIGHBOURS[0] == 0): self.x = self.x + 1
            elif(NEIGHBOURS[1] == 0) : self.x = self.x - 1
            elif(NEIGHBOURS[2] == 0) : self.y = self.y + 1
            elif(NEIGHBOURS[3] == 0) : self.y = self.y - 1
            else: super().collision(attacker, world)
        else:
            super().collision(attacker, world)


class CyberSheep(Animal):
    def __init__(self, x, y, world):
        self.image = CYBERSHEEP
        self.initiative = 4
        self.strength = 11
        super().__init__(x, y, world)

    def action(self, world):
        is_hogweed = 0
        X = []
        Y = []
        DISTANCE = []
        for i in world.Organisms:
            if(i.image == HOGWEED):
                is_hogweed = 1
                X.append(i.x)
                Y.append(i.y)
                DISTANCE.append(((self.x - i.x)**2) + ((self.y - i.y)**2))

        if(is_hogweed == 1):
            self.image = CYBERSHEEP
            min_index = DISTANCE.index(min(DISTANCE))

            if(X[min_index] > self.x): self.x = self.x + 1
            elif(X[min_index] < self.x): self.x = self.x - 1
            elif(Y[min_index] > self.y): self.y = self.y + 1
            elif(Y[min_index] < self.y): self.y = self.y - 1
        else:
            self.image = SHEEP
            super().action(world)

class Human(Animal):
    def __init__(self, x, y, world):
        self.image = HUMAN
        self.initiative = 4
        self.strength = 5
        self.move = 0
        self.abilityDuration = False
        self.abilityCount = 0
        super().__init__(x, y, world)


    def action(self, world):
        if(self.move == 1 and self.x < 19):
            self.x = self.x + 1
        elif(self.move == 2 and self.x > 0):
            self.x = self.x - 1
        elif(self.move == 3 and self.y < 19):
            self.y = self.y + 1
        elif(self.move == 4 and self.y > 0):
            self.y = self.y - 1

 
        if(self.move == 5 or self.abilityDuration == True):
            self.abilityCount = self.abilityCount + 1
            if(self.abilityCount <= 5):
                world.Comments.append("Human is using his sepcial ability")
                self.specialAbility(world)
                self.abilityDuration = True
            elif(self.abilityCount == 10):
                world.Comments.append("Human can use his special ability again")
                self.abilityDuration = False
                self.abilityCount = 0


        self.move = 0

    def specialAbility(self, world):
        for i in world.Organisms:
            if ((i.x == self.x and (i.y == self.y + 1 or i.y == self.y - 1)) or (i.y == self.y and (i.x == self.x + 1 or i.x == self.x - 1))):
                i.alive = False

                
            
        