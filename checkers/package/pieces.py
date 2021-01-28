import pygame as py
#from .boards import Board
from .constant import GREY, SQUARE_SIZE, WHITE, CROWN

class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king  = False

        if self.color == WHITE:
            self.direction = -1
        else :
            self. direction = 1
        
        self.x = 0
        self.y = 0
        self.calc_position()

    def calc_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king (self):
        self.king = True
    
    def draw_pieces(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        py.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        py.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))  

    def move_pieces(self,col,row):
        self.row = row
        self.col = col
        self.calc_position()

    def __repr__(self):
        return str(self.color)