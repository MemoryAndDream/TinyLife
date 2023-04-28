# -*- coding: utf-8 -*-
"""
Description :
date：          2023/4/11
"""
from environment import Environment
from xiaoyu import XiaoYu
from pygame.locals import *
import pygame,sys
import numpy as np

xiaoyu = XiaoYu()
xiaoyu.born(50,50,0.4)
# xiaoyu.inherit(r'E:\github\py3\TinyLife\data\grave\2023042621\1682517114224430.npz')
xiaoyu.mind.show()


size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
BLACK = (0, 0, 0)
RED  = (255, 0, 0)
BLUE  = (0, 0, 255)
clock = pygame.time.Clock()
bg=pygame.image.load(r"yu.png")

for i in range(1000):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(5) # fps
    xiaoyu.live()
    print(xiaoyu.hunger)
    screen.fill("white")
    env = xiaoyu.env.env
    rect = pygame.Rect(
        xiaoyu.x * 20,
        xiaoyu.y * 20,
        20, 20
    )
    # pygame.draw.rect(screen, BLUE, rect, 0)# 0填充
    bg1 = pygame.transform.rotate(bg,-90*xiaoyu.dirt)
    screen.blit(bg1, rect)

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
