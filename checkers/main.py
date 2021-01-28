import pygame as py
from package.game import Game
from package.constant import SQUARE_SIZE, WIDTH, HEIGHT
from package.boards import Board
from package.pieces import Piece

FPS = 60
WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption('Checkers')

def get_position_from_mouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row,col


def main():
    run = True
    clock = py.time.Clock()
    game = Game(WIN)
    while run :
        clock.tick(FPS)
        for event in py.event.get() :
            if event.type == py.QUIT:
                run = False
            if event.type == py.MOUSEBUTTONDOWN :
                position  = py.mouse.get_pos()
                row, col = get_position_from_mouse(position)
        
        game.update()


    py.quit()

main()