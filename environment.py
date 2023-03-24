# -*- coding: utf-8 -*-
"""
Description :
date：          2023/2/23
"""
import numpy as np
import random
class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.env = np.zeros((width, height),dtype=int) # 有食物的是1，没有的是0
        self.add_init_food()


    def add_init_food(self): # 随机生成食物 位置重叠就放弃
        print('init food')
        food_count = int(1000*1000/20)
        foods = []
        for i in range(food_count):
            w,h = random.randint(0,self.width-1),random.randint(0,self.width-1)
            food = (w,h)
            if not food in foods:
                foods.append(food)
        for food in foods:
           self.env[food[0],food[1]] = 1

        print('init food end')





    def refresh_food(self): #
        pass

if __name__ == '__main__':
    e = Environment(1000,1000)
    print(e.env)