import pygame as py
import sys

py.init()
clock = py.time.Clock()

#screen setup
scr_width = 800
scr_height = 600
screen = py.display.set_mode((scr_width,scr_height))
py.display.set_caption('pong by Alex_Freyjr')
bg_color = py.Color('grey10')
assets_color = py.Color('white')
screen.fill(bg_color)

#assets
ball =  py.Rect(scr_width/2 - 15, scr_height/2 - 15, 30,30)
paddle_p = py.Rect(scr_width - 20, scr_height/2 - 70,10,140)
paddle_b = py.Rect(10, scr_height/2 - 70, 10,140)
ball_speed_x = 7
ball_speed_y = 7
paddle_a_speed = 0

class Game:
    def __init__(self,screen,asset_color,rect_to_use,scr_width,scr_height):
        self.screen = screen
        self.asset_color = asset_color
        self.rect_to_use = rect_to_use
        self.scr_width = scr_width
        self.scr_height = scr_height

    def draw(self,rect_to_use):
    #base rectangle
        py.draw.rect(screen,assets_color,rect_to_use)
        py.draw.rect(screen,assets_color,rect_to_use)
        py.draw.ellipse(screen,assets_color,rect_to_use)
        py.draw.aaline(screen,assets_color, (scr_width/2,0), (scr_width/2,scr_height))


class Anim:
    def ball():
        global ball_speed_x, ball_speed_y
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= scr_height :
            ball_speed_y *= -1
        if ball.left <= 0 or ball.right >= scr_width :
            ball_speed_x *= -1
        if ball.colliderect(paddle_p) or ball.colliderect(paddle_b) :
            ball_speed_x *= -1

    def paddle_p():
        paddle_p.y += paddle_p_speed

        if paddle_p.top <=0:
            paddle_p.top=0
        if paddle_p.bottom >= scr_height:
            paddle_p.bottom = scr_height


#main loop
while True:
    #input
    for event in py.event.get():
        if event.type == py.QUIT :
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN :
            if event.key == py.K_s:
                paddle_p_speed += 7
            if event.key == py.K_w:
                paddle_p_speed -= 7
        if event.type == py.KEYUP :
            if event.key == py.K_s :
                paddle_p_speed -= 7
            if event.key == py.K_w :
                paddle_p_speed += 7
    
    ball_anim()
    paddle_anim()

    #update
    py.display.update()
    clock.tick(60)    
   