# -*- coding: utf-8 -*-
"""
Description :
date：          2023/4/11
"""
from environment import Environment
from diandian import DianDian
from pygame.locals import *
import pygame,sys
import numpy as np

diandian = DianDian()
diandian.born(50,50,0.2)
diandian.inherit(r'E:\github\py3\TinyLife\data\grave\last\16817833008442000.npz')
diandian.mind.show()


size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
BLACK = (0, 0, 0)
RED  = (255, 0, 0)
BLUE  = (0, 0, 255)
clock = pygame.time.Clock()

for i in range(1000):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(5) # fps
    diandian.live()
    print(diandian.hunger)
    screen.fill("white")
    env = diandian.env.env
    rect = pygame.Rect(
        diandian.x * 20,
        diandian.y * 20,
        20, 20
    )
    pygame.draw.rect(screen, BLUE, rect, 0)# 0填充
    for ix,iy  in np.ndindex(env.shape):
        if env[ix,iy]>=10:
            rect = pygame.Rect(
                ix * 20,
                iy * 20,
                20, 20
            )
            pygame.draw.rect(screen, BLACK, rect, 1)
        elif env[ix,iy]>0:
            v= env[ix, iy]
            rect = pygame.Rect(
                ix * 20,
                iy * 20,
                20, 20
            )

            pygame.draw.rect(screen, (int(v*255) if v<1 else 255, 0, 0), rect, 1)
    pygame.display.flip()
