# -*- coding: utf-8 -*-
"""
Description :
date：          2023/2/23
"""
import numpy as np
import random
from food import Food
class Environment:
    def __init__(self, width, height, food_rate=0.01):
        self.width = width
        self.height = height
        self.env = np.zeros((width, height),dtype=float) # 有食物的是1，没有的是0 dtype是int就不能扩散了！！
        self.foods = []
        self.food_rate = food_rate # 需要优化成平均多少有一个食物



    def loop(self, x, y):  # 测试地图有限，所以先循环一下 -1:999
        return x % self.width, y % self.height


    def refresh(self):
        # gen food with rate
        n = random.random()
        if n < self.food_rate:
            self.gen_food()
        for food in self.foods:
            food.life = food.life - 1
            if self.env[food.x,food.y] == 0: #eaten
                food.life = 0

        self.foods = [food for food in self.foods if food.life>0]
        self.refresh_food()

    def refresh_food(self):
        self.env = np.zeros((self.width, self.height), dtype=float)
        foods = self.foods
        for food in foods:
           self.env[food.x,food.y] = 10
           self.smell_spread(food.x,food.y)

    def gen_food(self):  # 随机生成食物 位置重叠就累加
        x, y = random.randint(0, self.width - 1), random.randint(0, self.width - 1)
        new_food = Food(x, y)
        self.foods.append(new_food)
        self.env[x, y] += 10
        self.smell_spread(x, y)


    def smell_spread(self,x,y):
        # 扩散浓度1/(r*r) 先只计算3格范围试试
        for w in range(-3,4):
            for h in range(-3, 4):
                if not w and not h:
                    continue
                loc_x,loc_y = self.loop(x+w,y+h)
                if self.env[loc_x, loc_y] < 10:
                    self.env[loc_x, loc_y] += 1/(w*w+h*h)

    def smell_disappear(self,x,y):
        for w in range(-3,4):
            for h in range(-3, 4):
                if not w and not h:
                    continue
                loc_x,loc_y = self.loop(x+w,y+h)
                if self.env[loc_x, loc_y] < 10:
                    self.env[loc_x, loc_y] -= 1/(w*w+h*h)



    def save_env(self):
        np.save('data/env.npy', self.env)

    def load_env(self):
        self.env = np.load('data/env.npy')

    def show(self):
        print(self.env)


if __name__ == '__main__':
    e = Environment(1000,1000, False)
