import pygame as py
import sys, random

def ball_anim():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= scr_height :
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= scr_width :
        ball_reset()
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b) :
        ball_speed_x *= -1
def ball_reset():
    global ball_speed_x, ball_speed_y
    ball.center = (scr_height/2, scr_width/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))
    if ball.left <= 0  :
        score_left += 1
    if ball.right >= scr_width :
        score_right += 1

def paddle_anim():
    paddle_a.y += paddle_a_speed

    if paddle_a.top <=0:
        paddle_a.top = 0
    if paddle_a.bottom >= scr_height:
        paddle_a.bottom = scr_height

def opponent_ai(): 
    if paddle_b.top < ball.y:
        paddle_b.top += paddle_b_speed
    if paddle_b.bottom > ball.y:
        paddle_b.bottom -= paddle_b_speed
    if paddle_b.top <=0:
        paddle_b.top = 0
    if paddle_b.bottom >= scr_height:
        paddle_b.bottom = scr_height



#init
py.init()
clock = py.time.Clock()
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
paddle_a_speed = 0
paddle_b_speed = 7
score_left = 0
score_right = 0

#screen setup
scr_width = 800
scr_height = 600
screen = py.display.set_mode((scr_width,scr_height))
py.display.set_caption('pong by Alex_Freyjr')
bg_color = py.Color('grey10')
assets_color = py.Color('white')

#base rectangle
ball =  py.Rect(scr_width/2 - 15, scr_height/2 - 15, 30,30)
paddle_a = py.Rect(scr_width - 20, scr_height/2 - 70,10,140)
paddle_b = py.Rect(10, scr_height/2 - 70, 10,140)

#main loop
while True:
    #input
    for event in py.event.get():
        if event.type == py.QUIT :
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN :
            if event.key == py.K_s:
                paddle_a_speed += 7
            if event.key == py.K_w:
                paddle_a_speed -= 7
        if event.type == py.KEYUP :
            if event.key == py.K_s :
                paddle_a_speed -= 7
            if event.key == py.K_w :
                paddle_a_speed += 7
    
    ball_anim()
    paddle_anim()
    opponent_ai()
    
    #visual
    screen.fill(bg_color)
    py.draw.rect(screen,assets_color,paddle_a)
    py.draw.rect(screen,assets_color,paddle_b)
    py.draw.ellipse(screen,assets_color,ball)
    py.draw.aaline(screen,assets_color, (scr_width/2,0), (scr_width/2,scr_height))

    #update
    py.display.update()
    clock.tick(60)    
   