import pygame

from constants import WIN, FONT
from Organism import Organism
from Animal import Animal



class World:
     def __init__(self):
         self.Organisms = []
         self.Comments = []

     def print(self):
         for i in self.Organisms:
             WIN.blit(i.image, (151 + i.x * 35, 51 + i.y * 35))

     def printComments(self):
         line = 0
         for i in self.Comments:
             textsurface = FONT.render(i, False, (0, 0, 0))
             WIN.blit(textsurface, (955,505 + line))
             line = line + 15

     def add(self, type):
         new_organism = type
         self.Organisms.append(new_organism)

     def makeTurn(self):
         size = self.Organisms.__len__()
         i = 0
         while i < self.Organisms.__len__():
                if(i < size and self.Organisms[i].alive):
                    self.Organisms[i].action(self)
                    self.Organisms[i].age = self.Organisms[i].age + 1

                j=0
                while j < self.Organisms.__len__():
                    if(i != j and self.Organisms[i].x == self.Organisms[j].x and self.Organisms[i].y == self.Organisms[j].y and self.Organisms[j].alive):
                        if(type(self.Organisms[i]) == type(self.Organisms[j])):
                            if(self.Organisms[i].age > 10 and self.Organisms[j].age > 10 and
                             self.Organisms[i].breeding_delay > 7 and self.Organisms[j].breeding_delay > 7):
                                self.Comments.append("A new " + type(self.Organisms[i]).__name__ + " has born")
                                (type(self.Organisms[i]))(self.Organisms[i].x, self.Organisms[i].y, self)
                                self.Organisms[i].breeding_delay = 0
                                self.Organisms[j].breeding_delay = 0
                                
                            self.Organisms[i].reverse_action()
                            self.Organisms[j].reverse_action()
                        elif self.Organisms[i].alive:
                            self.Organisms[j].collision(self.Organisms[i],self)
                    j = j + 1 

                i = i + 1               

     def kill(self):
         i = 0
         while i < self.Organisms.__len__():
                if(self.Organisms[i].alive == False):
                    self.Organisms.pop(i)
                    i= i - 1
                i = i + 1

     def sorting(self):
         self.Organisms.sort(key = lambda x: (x.initiative, x.age), reverse=True)