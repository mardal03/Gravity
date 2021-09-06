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

speed = 10
x = 0 - 15
y = 200

def draw():
    pygame.draw.circle(window, red, (250,250), 15)
    pygame.display.update()
    window.fill((0,0,0))

#def object():
    #speed = 5
    #x = (0 - 15)
    #y = 200
    #pygame.draw.circle(window, blue, (x, y), 15)
    
run = True
while run:
    keys = pygame.key.get_pressed()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x += speed

    pygame.draw.circle(window, blue, (x, y), 15)
    pygame.draw.circle(window, red, (250,250), 15)
    pygame.display.update()
    window.fill((0,0,0))
    
    

pygame.quit()