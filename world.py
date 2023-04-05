# -*- coding: utf-8 -*-
"""
Description :
date：          2023/4/5
"""
from diandian import DianDian
import os

def main():
    load_path = 'data/grave/202304051903'
    aged_diandians = []
    ages = []
    for root, dirs, files in os.walk(load_path):
        for file in files:
            path = os.path.join(root, file)
            diandian = DianDian()
            diandian.born()
            diandian.inherit(path)
            diandian.mind.mutate2()  # 进化！
            for t in range(3000):
                diandian.live(t)
                if not diandian.alive:
                    break

            aged_diandians.append(diandian)
            ages.append(diandian.age)
    aged_diandians = sorted(
        aged_diandians,
        key=lambda x:x.age,
    )
    new_ages = 0
    new_count = 0
    for aged_diandian in aged_diandians:
        if aged_diandian.age >= aged_diandians[int(len(aged_diandians)*1/2)].age:  # 筛选活的久的厚葬 每一代需要运行2次，不然人口下降
            aged_diandian.funeral(save_path='data/grave/202304051904')
            new_ages += aged_diandian.age
            new_count += 1
    # print(ages)
    print('上一代平均寿命:')
    print(sum(ages) / len(aged_diandians))
    print('筛选平均寿命:')
    print(new_ages / new_count)

if __name__ == '__main__':
    main()

