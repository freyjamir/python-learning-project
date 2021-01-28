from package.boards import Board
import pygame as py 
from .constant import WHITE
from .boards import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}
    
    def update(self):
        self.board.draw_board(self.win)
        py.display.update()

    def reset(self):
        self._init()
    
    def select(self,row,col):
        if self.selected:
            result = self._move(row,col)
            if not result :
                self.selected = None
                self.select(row,col)
        
        piece = self.board.get_piece(row,col)
        if piece != 0 and piece.color == self.turn:    
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)

    def _move(self,row,col):
        """
        docstring
        """
        pass