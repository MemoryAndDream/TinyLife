# -*- coding: utf-8 -*-
"""
Description :
date：          2023/2/23
"""
from environment import Environment
import random

class DianDian:
    def __init__(self):
        pass


    def born(self):
        w,h = 1000,1000
        self.env = Environment(w,h)
        self.x, self.y = random.randint(0, w-1), random.randint(0, h-1)
        self.hunger = 100  # 饥饿值
        self.age = 0  # 年龄 到1000生成10后代
        self.alive = True


    def show_status(self):
        print(f'location: {self.x} {self.y}')
        print(self.age,self.hunger)

    def move(self):
        dirt = random.choice([0,1,2,3])       # 1 随机移动
        if dirt == 0 and self.y > 0: # up
            self.y -= 1
        elif dirt == 1 and self.y < self.env.height-1: # down
            self.y += 1
        elif dirt == 2 and self.x > 0: # left
            self.x -= 1
        elif dirt == 3 and self.x < self.env.width-1: # right
            self.x += 1

    def move_origin(self,dirts): # 原始的移动不一定只有一个方向，单向移动也需要进化
        # 1 2 ,3 4互相抵消
        if 1 in dirts and 2 in dirts:
            dirts.remove(1)
            dirts.remove(2)
        if 3 in dirts and 4 in dirts:
            dirts.remove(3)
            dirts.remove(4)
        for dirt in dirts:
            if dirt == 0 and self.y > 0: # up
                self.y -= 1
            elif dirt == 1 and self.y < self.env.height-1: # down
                self.y += 1
            elif dirt == 2 and self.x > 0: # left
                self.x -= 1
            elif dirt == 3 and self.x < self.env.width-1: # right
                self.x += 1

    def eat(self):
        x, y = self.x, self.y
        if self.env.env[x, y] == 1:
            print('吃到了')
            self.env.env[x, y] = 0
            self.hunger += 10

    def grow(self):
        self.age += 1
        self.show_status()

    def live(self, time):
        self.hunger -= 1
        self.move()
        self.eat()
        self.grow()
        if self.hunger == 0:
            print('die')
            self.alive = False


if __name__ == '__main__':
    ages = []
    for i in range(100): # 100个点点
        diandian1 =  DianDian()
        diandian1.born()
        for t in range(1000):
            diandian1.live(t)
            if not diandian1.alive:
                ages.append(diandian1.age)
                break
    print(ages)
    print(float(sum(ages)) / len(ages) )

