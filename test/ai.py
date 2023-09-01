# -*- coding: utf-8 -*-
"""
File Name：     ai
Description :
Author :       meng_zhihao
mail :       312141830@qq.com
date：          2023/8/28
"""



class Concept:
    def __init__(self,name):
        self.id = id(self)
        self.name = name



class Path:
    def __init__(self,start,end,last_activate=0,long_activate=0):
        self.id = id(self)
        self.start = start
        self.end = end
        self.last_activate = last_activate
        self.long_activate = long_activate # 因为是抽象概念

    def activate(self, t):
        self.long_activate += 1
        self.last_activate = t

    def split(self): # 只有激活区间需要分裂
        mid_concept = Concept('mid')
        new_path1 = Path(self.start, mid_concept.id,self.last_activate,self.long_activate)
        new_path2 = Path(mid_concept.id, self.end,self.last_activate,self.long_activate)
        return new_path1,new_path2

    def can_activate(self,t): # 抽象概念路径激活函数 取消概率观点，直接省略低系数路径 参考最长记忆长度 回忆的时候确认
        longa = self.long_activate
        lasta =  self.last_activate
        delt = t - lasta
        s = longa + 10/delt
        return s>3

def memory():


    start = Concept('in')
    a = Concept('a')
    b = Concept('b')
    c = Concept('c')
    d = Concept('d')

    t = 0
    # 记忆过程
    # 输入a 生成路径 in-a
    paths = []
    outs = []
    outs.append(a)
    newpath = Path(start.id,a.id)
    newpath.activate(t)
    paths.append(newpath)

    # 输入b 基于原先路径生成新路径 并增强公用路径
    t += 1
    newpaths = []
    for path in paths:
        if path.can_activate(t):
            path.split()



# 迭代
# 疲劳

# 连接本来就存在，只是点亮了罢了


# 记忆abcd # 实验需不需要start节点
if __name__ == '__main__':
    memory()

