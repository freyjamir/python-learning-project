import pygame as py

WIDTH = 800
HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH//COLS

#add rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128,128)

CROWN = py.transform.scale(py.image.load('assets/crown.png'), (45,30))