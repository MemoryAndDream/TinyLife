# -*- coding: utf-8 -*-
"""
Description :
date：          2023/2/23
"""
from environment import Environment
import random
from mind import Mind
import numpy as np
import time
import os


class XiaoYu:
    def __init__(self):
        pass

    def born(self, w=1000, h=1000, food_rate=0.1):
        self.env = Environment(w, h, food_rate)
        self.x, self.y = random.randint(0, w - 1), random.randint(0, h - 1)
        self.hunger = 200  # 饥饿值
        self.age = 0  # 年龄 到1000生成10后代
        self.alive = True
        self.mind = Mind()
        self.name = str(int(time.time() * 1000))
        self.dirt = 1  # 方向 0 1 2 3: up  right down   left

    def inherit(self, brain_file):
        self.mind.load(brain_file)

    def show_status(self):
        print(f'location: {self.x} {self.y}')
        print(self.age, self.hunger)

    def see(self):  # 边界待考虑
        x = self.x
        y = self.y
        left_inputs = 0
        right_inputs = 0
        for food in self.env.foods:
            if food.x==x and food.y == y: # 完全重叠的不算，但是同一行还是要看方向的
                continue
            if self.dirt == 0: # up
                if food.x> x:
                    right_inputs += self.env.cal_sight(x, y, food.x, food.y, self.dirt)
                else:
                    left_inputs += self.env.cal_sight(x, y, food.x, food.y, self.dirt)
            elif self.dirt == 1: # right
                if food.y> y:
                    right_inputs  += self.env.cal_sight(x, y, food.x, food.y, self.dirt)
                else:
                    left_inputs += self.env.cal_sight(x, y, food.x, food.y, self.dirt)
            elif self.dirt == 2: # down
                if food.x< x:
                    right_inputs += self.env.cal_sight(x, y, food.x, food.y, self.dirt)
                else:
                    left_inputs += self.env.cal_sight(x, y, food.x, food.y, self.dirt)
            elif self.dirt == 3: # left
                if food.y< y:
                    right_inputs += self.env.cal_sight(x, y, food.x, food.y, self.dirt)
                else:
                    left_inputs += self.env.cal_sight(x, y, food.x, food.y, self.dirt)

        boundary_input = np.array([self.check_boundary()])

        return left_inputs, right_inputs, boundary_input

    def check_boundary(self):  # 撞墙视为1
        dirt = self.dirt
        x, y = self.x, self.y
        if dirt == 0:  # up
            y -= 1
        elif dirt == 1:  # right
            x += 1
        elif dirt == 2:  # down
            y += 1
        elif dirt == 3:  # left
            x -= 1
        return 0 if self.env.in_boundary(x, y) else 1

    def think_and_move(self):  # 前进转向都消耗能量。而且左右同时触发转向白白消耗能量
        left_inputs, right_inputs, boundary_input = self.see()
        turn_left, forward, turn_right = self.mind.response([left_inputs, right_inputs], boundary_input)
        if turn_left:
            # self.hunger -= 0.3
            self.dirt = (self.dirt- 1)%4
        if turn_right:
            # self.hunger -= 0.3
            self.dirt = (self.dirt+ 1)%4
        if forward:
            # self.hunger -= 0.3
            self.move()

    def move(self):
        dirt = self.dirt
        x, y = self.x, self.y
        if dirt == 0:  # up
            y -= 1
        elif dirt == 1:  # right
            x += 1
        elif dirt == 2:  # down
            y += 1
        elif dirt == 3:  # left
            x -= 1
        if self.env.in_boundary(x, y):
            self.x, self.y = x, y


    def eat(self):
        x, y = self.x, self.y
        if self.env.env[x, y] >= 10:
            self.hunger += self.env.env[x, y]
            self.env.env[x, y] = 0
            # self.env.show()

    def grow(self):
        self.age += 1
        # self.show_status()

    def live(self):
        self.env.refresh()
        self.hunger -= 1
        self.think_and_move()
        self.eat()
        self.grow()
        if self.hunger <= 0:
            self.alive = False
            # self.funeral()

    def funeral(self, save_path=None):  # 送走
        self.mind.save(self.name, self.age, save_path)


def main():
    ages = []
    for i in range(1000):
        print('第 %s 只' % (i + 1))
        diandian = XiaoYu()
        diandian.born(50,50,0.4)
        diandian.mind.mutate()  # 进化！
        # diandian.mind.show()
        for t in range(1000):
            diandian.live()
            if not diandian.alive:
                ages.append(diandian.age)
                if diandian.age > 300:  # 筛选活的久的厚葬
                    diandian.funeral()
                break
        print(diandian.age)
    # print(ages)
    print('平均寿命')
    print(float(sum(ages)) / len(ages))




if __name__ == '__main__':
    main() #  随机个体测试， 复杂测试在world
    # reload()
