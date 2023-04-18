# -*- coding: utf-8 -*-
"""
Description :
date：          2023/4/10
"""
from pygame.locals import *

import pygame,sys
# screen = pygame.display.set_mode((1000, 1000), 0, 32)

size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)

WIDTH,HEIGHT = 100,100
pygame.display.set_caption('diandian')
# 设置背景颜色
screen.fill((255, 255, 255))
# 更新屏幕
pygame.display.update()
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
WHITE = (255, 255, 255)
BOARD_PADDING = 20
board_width = ((2 / 3) * width) - (BOARD_PADDING * 2)
board_height = height - (BOARD_PADDING * 2)
cell_size = int(min(board_width / WIDTH, board_height / HEIGHT))
board_origin = (BOARD_PADDING, BOARD_PADDING)


for i in range(100):
    row = []
    for j in range(100):
        # 为单元格绘制矩形

        rect = pygame.Rect(
            board_origin[0] + j * 10,
            board_origin[1] + i * 10,
            10, 10
        )
        pygame.draw.rect(screen, BLACK, rect,1)
        # pygame.draw.rect(screen, WHITE, rect, 3)
pygame.display.update()
# screen.blit(buttonText, buttonRect) 刷新区域

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("white")

画图展示的时候用小地图，30*30来看和测试！！