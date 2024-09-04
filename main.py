import pygame
import random

pygame.init()

screen_width=800
screen_height=600

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Выживи с шарами 1234")
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)

square_size=50
square_x=screen_width//2
square_y=screen_height-square_size

ball_radius=15
ball_x=screen_width//2
ball_y=screen_height-square_size

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]and square_x>0:
            square_x = square_x-23
        if keys[pygame.K_RIGHT]and square_x<screen_width-square_size:
            square_x= square_x+23
        if keys[pygame.K_UP]and square_y>0:
            square_y = square_y-23
        if keys[pygame.K_DOWN]and square_y<screen_height-square_size:
            square_y = square_y+23
        
    ball_y=ball_y+1
    if ball_y>screen_height:
        ball_y=0
        ball_x=random.randint(0,screen_width)

    screen.fill(WHITE)
    pygame.draw.rect(screen,BLUE,(square_x,square_y,square_size,square_size))
    pygame.draw.circle(screen,GREEN,(ball_x,ball_y),ball_radius)
    pygame.display.update()
