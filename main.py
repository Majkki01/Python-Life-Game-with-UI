#Author: Michał Rejmak, s184464, II sem, Data Engineering

import pygame
import os
import time
import sys

from pygame.constants import K_x, MOUSEBUTTONDOWN
from constants import *
from World import World
from Organism import Organism
from Animal import *
from Plant import *
from GameState import GameState

pygame.display.set_caption("LIFE! THE GAME")

ORG_NUMBERS = {
    0 : Wolf,
    1 : Sheep,
    2 : Fox,
    3 : Turtle,
    4 : Antelope,
    5 : CyberSheep,
    6 : Grass,
    7 : SowThistle,
    8 : Guarana,
    9 : Belladonna,
    10 : SosnowskysHogweed,
    11 : Human
}

def draw_window(world):
    WIN.blit(BACKGROUND, (0,0))
    WIN.blit(TABLE_IMAGE, (150,50))
    pygame.draw.rect(WIN, WHITE, (950, 50, 250, 700))

    if TITLE_RECT.collidepoint(pygame.mouse.get_pos()): WIN.blit(TITLE2, (950,50))
    else: WIN.blit(TITLE, (950,50))

    if NEW_RECT.collidepoint(pygame.mouse.get_pos()): WIN.blit(NEW_GAME2, (950,150))
    else: WIN.blit(NEW_GAME, (950,150))

    if LOAD_RECT.collidepoint(pygame.mouse.get_pos()): WIN.blit(LOAD_GAME2, (950,250))
    else: WIN.blit(LOAD_GAME, (950,250))

    if SAVE_RECT.collidepoint(pygame.mouse.get_pos()): WIN.blit(SAVE_GAME2, (950,350))
    else: WIN.blit(SAVE_GAME, (950,350))

    WIN.blit(COMMENTS, (950,450))
    WIN.blit(COM_FRAME, (950,450))

    if NEXT_RECT.collidepoint(pygame.mouse.get_pos()): WIN.blit(NEXT2, (1075,700))
    else: WIN.blit(NEXT, (1075,700))

    if ABILITY_RECT.collidepoint(pygame.mouse.get_pos()): WIN.blit(ABILITY2, (950,700))
    else: WIN.blit(ABILITY, (950,700))

    if TABLE_RECT.collidepoint(pygame.mouse.get_pos()):
        POS = pygame.mouse.get_pos()
        x = POS[0]
        y = POS[1]

        x = (x - 151) // 35
        y = (y - 51) // 35

        x_cor = x
        y_cor = y
       
        x = (x * 35) + 151
        y = (y * 35) + 51

        is_free = True
        for i in world.Organisms:
            if x_cor == i.x and y_cor == i.y:
                is_free = False
                break
                    
        if is_free == True:
            WIN.blit(CELL, (x, y))


    world.print()
    world.printComments()
    pygame.display.update()
    
def spawn_organisms(W):
    g1 = Grass(7,14,W)
    g2 = Grass(0,12,W)
    g3 = Grass(19,2,W)

    st1 = SowThistle(13,12,W)
    st2 = SowThistle(7,1,W)
    st3 = SowThistle(16,9,W)

    g1 = Guarana(14,17,W)
    g2 = Guarana(2,18,W)
    g3 = Guarana(4,0,W)

    b1 = Belladonna(10,7,W)
    b2 = Belladonna(6,16,W)
    b3 = Belladonna(14,1,W)

    sh1 = SosnowskysHogweed(11,4,W)
    sh2 = SosnowskysHogweed(9,16,W)
    sh3 = SosnowskysHogweed(18,8,W)


    w1 = Wolf(2,3,W)
    w2 = Wolf(2,14,W)
    w3 = Wolf(16,3,W)
    w4 = Wolf(2,5,W)
    w5 = Wolf(2,7,W)
    w6 = Wolf(4,14,W)

    s1 = Sheep(15,15,W)
    s2 = Sheep(6,3,W)
    s3 = Sheep(13,19,W)
    s4 = Sheep(17,15,W)
    s5 = Sheep(19,15,W)
    s6 = Sheep(11,19,W)

    f1 = Fox(9,13,W)
    f2 = Fox(1,18,W)
    f3 = Fox(11,11,W)

    t1 = Turtle(0,7,W)
    t2 = Turtle(18,0,W)
    t3 = Turtle(4,8,W)

    a1 = Antelope(8,5,W)
    a2 = Antelope(18,12,W)
    a3 = Antelope(3,10,W)

    cs1 = CyberSheep(7,10,W)
    cs2 = CyberSheep(15,5,W)
    cs3 = CyberSheep(17,18,W)

    h1 = Human(10,9,W)

def manual_spawn(x , y, world):
    selected = False
    while selected == False:
        WIN.blit(CHOICE_MENU, (490,350))
        WIN.blit(WOLF, (516,362))
        WIN.blit(SHEEP, (559,362))
        WIN.blit(FOX, (602,362))
        WIN.blit(TURTLE, (645,362))
        WIN.blit(ANTELOPE, (688,362))
        WIN.blit(CYBERSHEEP,(731,362))
        WIN.blit(GRASS, (516,405))
        WIN.blit(SOW_THISTLE, (559,405))
        WIN.blit(GUARANA, (602,405))
        WIN.blit(BELLADONNA, (645,405))
        WIN.blit(HOGWEED, (688,405))
        WIN.blit(HUMAN,(731,405))

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                org_nr = -1
                for i in range(12):
                    if CHOICE_RECTS[i].collidepoint(pygame.mouse.get_pos()):
                        org_nr = i
                        selected = True
                        break
                
                if selected:
                    ORG_NUMBERS[org_nr](x,y,world)
                        
        pygame.display.update()


def main():
    W = World()
    STATE = GameState()

    run = True

    while run:
        for event in pygame.event.get():
            maketurn = 0

            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.KEYDOWN:
                for i in W.Organisms:
                    if type(i) == Human:
                        if event.key == pygame.K_RIGHT:
                            i.move = 1
                            maketurn = 1
                        elif event.key == pygame.K_LEFT:
                            i.move = 2
                            maketurn = 1
                        elif event.key == pygame.K_DOWN:
                            i.move = 3
                            maketurn = 1
                        elif event.key == pygame.K_UP:
                            i.move = 4
                            maketurn = 1
                

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if NEW_RECT.collidepoint(pygame.mouse.get_pos()):
                    spawn_organisms(W)
                elif LOAD_RECT.collidepoint(pygame.mouse.get_pos()):
                    STATE.load(W)
                elif SAVE_RECT.collidepoint(pygame.mouse.get_pos()):
                    STATE.save(W)
                elif TITLE_RECT.collidepoint(pygame.mouse.get_pos()):
                    W.Organisms.clear()
                elif NEXT_RECT.collidepoint(pygame.mouse.get_pos()):
                    maketurn = 1
                elif ABILITY_RECT.collidepoint(pygame.mouse.get_pos()):
                    for i in W.Organisms:
                        if type(i) == Human:
                            i.move = 5
                    maketurn = 1
                elif TABLE_RECT.collidepoint(pygame.mouse.get_pos()):
                    POS = pygame.mouse.get_pos()
                    x = POS[0]
                    y = POS[1]

                    x = (x - 151) // 35
                    y = (y - 51) // 35

                    is_free = True
                    for i in W.Organisms:
                        if x == i.x and y == i.y:
                            is_free = False
                            break
                    
                    if is_free == True:
                        manual_spawn(x,y,W)
    

            if maketurn == 1:
                W.Comments.clear()
                W.sorting()
                W.makeTurn()
                W.kill()

    

        draw_window(W)
        
    pygame.quit()

if __name__ == "__main__":
    main()