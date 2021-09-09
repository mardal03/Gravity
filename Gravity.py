# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:17:35 2021

@author: mariu
"""

import pygame
import math

pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((500, 500))

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

vel = 5
as_x = 0 - 15
as_y = 100

sun_x = 250
sun_y = 250

def draw():
    pygame.draw.circle(window, red, (sun_x, sun_y), 15)
    pygame.draw.circle(window, blue, (as_x, as_y), 15)
    pygame.display.update()
    window.fill(black)
    
def gravity():
    if as_x < sun_x:
        dis = math.sqrt(((sun_x-as_x)*(sun_x-as_x))+((sun_y-as_y)*(sun_y-as_y)))
    elif as_x > sun_x:
        dis = math.sqrt(((as_x-sun_x)*(as_x-sun_x))+((sun_y-as_y)*(sun_y-as_y)))
    else:
        dis = sun_y-as_y
    print(dis)
    
    if dis < 200:
        pass

run = True
while run:
    keys = pygame.key.get_pressed()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #if keys[pygame.K_SPACE]:
    as_x += vel

    draw()
    gravity()
pygame.quit()