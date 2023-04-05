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
        try:
            self.load_env()
        except FileNotFoundError as e:
            print(e)
            self.add_init_food()
            self.save_env()

    def loop(self, x, y):  # 测试地图有限，所以先循环一下 -1:999
        return x % self.width, y % self.height

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
           self.env[food[0],food[1]] = 10
           self.smell_spread(food[0],food[1])

        print('init food end')

    def smell_spread(self,x,y):
        # 扩散浓度1/(r*r) 先只计算3格范围试试
        for w in range(-3,4):
            for h in range(-3, 4):
                if not w and not h:
                    continue
                loc_x,loc_y = self.loop(x+w,y+h)
                self.env[loc_x, loc_y] = 1/(w*w+h*h)







    def save_env(self):
        np.save('data/env.npy', self.env)

    def load_env(self):
        self.env = np.load('data/env.npy')




    def refresh_food(self): #
        pass

if __name__ == '__main__':
    e = Environment(1000,1000)
