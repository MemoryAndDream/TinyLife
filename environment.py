# -*- coding: utf-8 -*-
"""
Description :
date：          2023/2/23
"""
import numpy as np
import random
from food import Food
class Environment:
    def __init__(self, width, height, food_rate=0.01): #左上角视为0,0！与pygame一致
        self.width = width
        self.height = height
        self.env = np.zeros((width, height),dtype=float) # 有食物的是1，没有的是0 dtype是int就不能扩散了！！
        self.foods = []
        self.food_rate = food_rate # 需要优化成平均多少有一个食物

    def get(self,x,y): # 获取env值，处理边界条件
        if self.in_boundary(x,y):
            return self.env[x,y]
        else:
            return 0


    def in_boundary(self,x,y):
        if x>=0 and  y>=0 and x<self.width and y<self.height:
            return True
        else:
            return False


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

    def gen_food(self):  # 随机生成食物 位置重叠就累加
        x, y = random.randint(0, self.width - 1), random.randint(0, self.width - 1)
        new_food = Food(x, y)
        self.foods.append(new_food)
        self.env[x, y] += 10


    def cal_sight(self,eye_x, eye_y, food_x, food_y,dirt ): # 计算眼睛看到的光亮  角度* r * r 眼睛先用180度计算
        x = abs(food_x-eye_x)
        y = abs(food_y-eye_y)
        r2 = x * x + y * y
        r = r2** 0.5
        if dirt in [0,2]:#上下朝向
            theta = x/r
        else:
            theta = y/r
        return 100*theta/r2 # 不乘10视力太差了



    def save_env(self):
        np.save('data/env.npy', self.env)

    def load_env(self):
        self.env = np.load('data/env.npy')

    def show(self):
        print(self.env)


if __name__ == '__main__':
    e = Environment(1000,1000, False)
