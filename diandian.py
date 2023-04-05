# -*- coding: utf-8 -*-
"""
Description :
date：          2023/2/23
"""
from environment import Environment
import random
from diandian_brain import DianDianBrain
import numpy as np
import time
import os

class DianDian:
    def __init__(self):
        pass

    def born(self):
        w, h = 1000, 1000
        self.env = Environment(w, h)
        self.x, self.y = random.randint(0, w - 1), random.randint(0, h - 1)
        self.hunger = 100  # 饥饿值
        self.age = 0  # 年龄 到1000生成10后代
        self.alive = True
        self.mind = DianDianBrain()
        self.name = str(int(time.time() * 1000))

    def inherit(self, brain_file):
        self.mind.load(brain_file)



    def show_status(self):
        print(f'location: {self.x} {self.y}')
        print(self.age,self.hunger)

    def move_random(self):
        dirt = random.choice([0, 1, 2, 3])  # 1 随机移动 左上角为0,0
        if dirt == 0 and self.y > 0:  # up
            self.y -= 1
        elif dirt == 1 and self.y < self.env.height - 1:  # down
            self.y += 1
        elif dirt == 2 and self.x > 0:  # left
            self.x -= 1
        elif dirt == 3 and self.x < self.env.width - 1:  # right
            self.x += 1


    def circle(self, x, y):  # 测试地图有限，所以先循环一下 -1:999
        return x % self.env.width, y % self.env.height

    def get_surrounding(self):  # 边界待考虑
        x = self.x
        y = self.y
        surrounding = np.array([self.env.env[self.circle(x - 1, y - 1)], self.env.env[self.circle(x, y - 1)],
                                self.env.env[self.circle(x + 1, y - 1)],
                                self.env.env[self.circle(x - 1, y)],
                                self.env.env[self.circle(x + 1, y)], self.env.env[self.circle(x - 1, y + 1)],
                                self.env.env[self.circle(x, y + 1)], self.env.env[self.circle(x + 1, y + 1)]])
        return surrounding

    def move(self):
        move_dirts = self.mind.feedforward(self.get_surrounding())
        dirts = []
        for i in range(len(move_dirts)):
            if move_dirts[i]:
                dirts.append(i)

        self.move_with_dirt(dirts)

    def move_with_dirt(self, dirts):  # 原始的移动不一定只有一个方向，单向移动也需要进化
        # 地图循环
        for dirt in dirts:
            if dirt == 0:  # up
                self.y -= 1
            elif dirt == 1:  # down
                self.y += 1
            elif dirt == 2:  # left
                self.x -= 1
            elif dirt == 3:  # right
                self.x += 1
        self.x, self.y = self.circle(self.x, self.y)

    def eat(self):
        x, y = self.x, self.y
        if self.env.env[x, y] == 1:
            # print('吃到了')
            self.env.env[x, y] = 0
            self.hunger += 10

    def grow(self):
        self.age += 1
        # self.show_status()

    def live(self, time):
        self.hunger -= 1
        self.move()
        self.eat()
        self.grow()
        if self.hunger == 0:
            self.alive = False
            # self.funeral()

    def funeral(self, save_path=None):  # 送走
        self.mind.save(self.name, self.age, save_path)


def main():
    ages = []
    for i in range(1000):
        print('第 %s 只点点' % (i + 1))
        diandian = DianDian()
        diandian.born()
        diandian.mind.mutate()  # 进化！
        for t in range(1000):
            diandian.live(t)
            if not diandian.alive:
                ages.append(diandian.age)
                if diandian.age > 500:  # 筛选活的久的厚葬
                    diandian.funeral()

                break
    # print(ages)
    print('平均寿命')
    print(float(sum(ages)) / len(ages))

def reload(): # 从老样本载入作为父本继续突变
    load_path = 'data/grave/2023040323'
    ages = []
    for root, dirs, files in os.walk(load_path):
        for file in files:
            path = os.path.join(root, file)
            diandian = DianDian()
            diandian.born()
            diandian.inherit(path)
            diandian.mind.mutate2()  # 进化！
            for t in range(1000):
                diandian.live(t)
                if not diandian.alive:
                    ages.append(diandian.age)
                    if diandian.age > 500:  # 筛选活的久的厚葬
                        diandian.funeral()
                        break
    # print(ages)
    print('平均寿命')
    print(float(sum(ages)) / len(ages))

if __name__ == '__main__':
    # main()
    reload()