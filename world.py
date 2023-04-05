# -*- coding: utf-8 -*-
"""
Description :
date：          2023/4/5
"""
from diandian import DianDian
import os
import shutil

def main():
    load_path = 'data/grave/last'
    save_path = 'data/grave/new'
    if os.path.exists(load_path) and os.path.exists(save_path):
        shutil.rmtree(load_path)
        os.rename(save_path, load_path)


    aged_diandians = []
    ages = []
    competition_rate = 3 # how many childs for a parent make
    for i in range(competition_rate):
        for root, dirs, files in os.walk(load_path):
            for file in files:
                path = os.path.join(root, file)
                diandian = DianDian()
                diandian.born()
                diandian.inherit(path)
                diandian.mind.mutate2()  # 进化！
                for t in range(20000):
                    diandian.live(t)
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


if __name__ == '__main__':
    for i in range(10):
        main()

