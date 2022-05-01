import types
import pygame
import os

WIDTH = 1280
HEIGHT = 800

WHITE = (255,255,255) 

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.font.init()
FONT = pygame.font.SysFont('arial', 10)

TABLE_IMAGE = pygame.image.load(os.path.join('PICTURES', 'Table.png'))
TABLE_RECT = TABLE_IMAGE.get_rect(x = 150 ,y = 50)
BACKGROUND = pygame.image.load(os.path.join('PICTURES', 'background.bmp'))
TITLE = pygame.image.load(os.path.join('PICTURES', 'title.png'))
TITLE2 = pygame.image.load(os.path.join('PICTURES', 'title2.png'))
TITLE_RECT = TITLE.get_rect(x = 950, y = 50)
NEW_GAME = pygame.image.load(os.path.join('PICTURES', 'new_game.png'))
NEW_GAME2 = pygame.image.load(os.path.join('PICTURES', 'new_game2.png'))
NEW_RECT = NEW_GAME.get_rect(x = 950, y = 150)
LOAD_GAME = pygame.image.load(os.path.join('PICTURES', 'load_game.png'))
LOAD_GAME2 = pygame.image.load(os.path.join('PICTURES', 'load_game2.png'))
LOAD_RECT = LOAD_GAME.get_rect(x = 950, y = 250)
SAVE_GAME = pygame.image.load(os.path.join('PICTURES', 'save_game.png'))
SAVE_GAME2 = pygame.image.load(os.path.join('PICTURES', 'save_game2.png'))
SAVE_RECT = SAVE_GAME.get_rect(x = 950, y = 350)
COMMENTS = pygame.image.load(os.path.join('PICTURES', 'comments.png'))
COM_FRAME = pygame.image.load(os.path.join('PICTURES', 'comm_frame.png'))
NEXT = pygame.image.load(os.path.join('PICTURES', 'next.png'))
NEXT2 = pygame.image.load(os.path.join('PICTURES', 'next2.png'))
NEXT_RECT = NEXT.get_rect(x = 1075, y = 700)
ABILITY = pygame.image.load(os.path.join('PICTURES', 'human_ab.png'))
ABILITY2 = pygame.image.load(os.path.join('PICTURES', 'human_ab2.png'))
ABILITY_RECT = ABILITY.get_rect(x = 950, y = 700)
CELL = pygame.image.load(os.path.join('PICTURES', 'cell.png'))
CHOICE_MENU = pygame.image.load(os.path.join('PICTURES', 'choice_menu.png'))

CHOICE_RECTS = []

for i in range(12):
    if i < 6: CHOICE_RECTS.append(pygame.Rect(516 + (i*43),362,33,33))
    else: CHOICE_RECTS.append(pygame.Rect(516 + ((i-6)*43),405,33,33))


HUMAN = pygame.image.load(os.path.join('PICTURES', 'tom.png'))

WOLF = pygame.image.load(os.path.join('PICTURES', 'wolf.png'))
SHEEP = pygame.image.load(os.path.join('PICTURES', 'sheep.png'))
FOX = pygame.image.load(os.path.join('PICTURES', 'fox.png'))
TURTLE = pygame.image.load(os.path.join('PICTURES', 'turtle.png'))
ANTELOPE = pygame.image.load(os.path.join('PICTURES', 'antelope.png'))
CYBERSHEEP = pygame.image.load(os.path.join('PICTURES', 'cybersheep.png'))

GRASS = pygame.image.load(os.path.join('PICTURES', 'grass.png'))
SOW_THISTLE = pygame.image.load(os.path.join('PICTURES', 'sow_thistle.png'))
GUARANA = pygame.image.load(os.path.join('PICTURES', 'guarana.png'))
BELLADONNA = pygame.image.load(os.path.join('PICTURES', 'belladonna.png'))
HOGWEED = pygame.image.load(os.path.join('PICTURES', 'hogweed.png'))

