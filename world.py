# -*- coding: utf-8 -*-
"""

"""
from xiaoyu import XiaoYu
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


    aged_xiaoyus = []
    ages = []
    competition_rate = 10 # how many childs for a parent make
    for i in range(competition_rate):
        for root, dirs, files in os.walk(load_path):
            for file in files:
                path = os.path.join(root, file)
                xiaoyu = XiaoYu()
                xiaoyu.born(50,50, food_rate=0.25)
                xiaoyu.inherit(path)
                xiaoyu.mind.mutate3()
                for t in range(2000):
                    xiaoyu.live()
                    if not xiaoyu.alive:
                        break
                aged_xiaoyus.append(xiaoyu)
                ages.append(xiaoyu.age)

    aged_xiaoyus = sorted(
        aged_xiaoyus,
        key=lambda x:x.age,
    )
    for aged_xiaoyu in aged_xiaoyus[-int(len(aged_xiaoyus)/competition_rate):]:
        aged_xiaoyu.funeral(save_path=save_path)
    # print(ages)
    print('本代平均寿命:')
    average = sum(ages) / len(aged_xiaoyus)
    print(average)



def random_mutate(): # 随机生成 1000个取最高
    save_path = 'data/grave/new'
    if not os.path.exists(save_path):
        os.mkdir (save_path)
    aged_xiaoyus = []
    ages = []
    for i in range(1000):
        xiaoyu = XiaoYu()
        xiaoyu.born(50,50, food_rate=0.3)
        xiaoyu.mind.mutate()
        for t in range(1000):
            xiaoyu.live()
            if not xiaoyu.alive:
                break
        aged_xiaoyus.append(xiaoyu)
        ages.append(xiaoyu.age)

    aged_xiaoyus = sorted(
        aged_xiaoyus,
        key=lambda x:x.age,
    )
    aged_xiaoyus[-1].funeral(save_path=save_path)

    print('最高寿命：',aged_xiaoyus[-1].age)


if __name__ == '__main__':
    random_mutate()
    # for i in range(1):
    #     random_mutate()

