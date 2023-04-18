# -*- coding: utf-8 -*-
"""
Description :
date：          2023/4/5
"""
from diandian import DianDian
import os
import shutil

def mutate(): # 遗传优化
    load_path = 'data/grave/last'
    save_path = 'data/grave/new'
    if os.path.exists(load_path) and os.path.exists(save_path):
        shutil.rmtree(load_path)
        os.rename(save_path, load_path)
    if not os.path.exists(load_path):
        return


    aged_diandians = []
    ages = []
    competition_rate = 10 # how many childs for a parent make
    for i in range(competition_rate):
        for root, dirs, files in os.walk(load_path):
            for file in files:
                path = os.path.join(root, file)
                diandian = DianDian()
                diandian.born(50,50, food_rate=0.25)
                diandian.inherit(path)
                diandian.mind.mutate3()
                for t in range(2000):
                    diandian.live()
                    if not diandian.alive:
                        break
                aged_diandians.append(diandian)
                ages.append(diandian.age)

    aged_diandians = sorted(
        aged_diandians,
        key=lambda x:x.age,
    )
    for aged_diandian in aged_diandians[-int(len(aged_diandians)/competition_rate):]:
        aged_diandian.funeral(save_path=save_path)
    # print(ages)
    print('本代平均寿命:')
    average = sum(ages) / len(aged_diandians)
    print(average)



def random_mutate(): # 随机生成 1000个取最高
    save_path = 'data/grave/new'
    if not os.path.exists(save_path):
        os.mkdir (save_path)
    aged_diandians = []
    ages = []
    for i in range(3000):
        diandian = DianDian()
        diandian.born(50,50, food_rate=0.3)
        diandian.mind.mutate4()
        for t in range(1000):
            diandian.live()
            if not diandian.alive:
                break
        aged_diandians.append(diandian)
        ages.append(diandian.age)

    aged_diandians = sorted(
        aged_diandians,
        key=lambda x:x.age,
    )
    aged_diandians[-1].funeral(save_path=save_path)

    print('最高寿命：',aged_diandians[-1].age)


if __name__ == '__main__':
    for i in range(200):
        mutate()

