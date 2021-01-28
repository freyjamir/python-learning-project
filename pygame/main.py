import pygame as py
import os

WIDTH, HEIGHT = 900, 500
WIN = py.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
FPS = 60
py.display.set_caption("game")


def draw_windows():
    WIN.fill(WHITE)
    py.display.update()

def main():
    clock = py.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
    draw_windows()
    py.quit()

if __name__ == "__main__":
    main()