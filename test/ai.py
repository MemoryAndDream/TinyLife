# -*- coding: utf-8 -*-
"""
File Name：     ai
Description :
Author :       meng_zhihao
mail :       312141830@qq.com
date：          2023/8/28
"""

NEURON_DICT = {}

class Concept:
    def __init__(self,name):
        self.id = id(self)
        self.name = name
        NEURON_DICT[self.id]=name



class Path:
    def __init__(self,start,end,last_activate=0,attenuation=1024.0,deepth=1):
        self.id = id(self)
        self.start = start
        self.end = end
        self.last_activate = last_activate
        self.attenuation = attenuation # 衰减系数，初始值设置为1024
        self.deepth = deepth

    def activate(self, t):
        self.attenuation = 0.9*self.attenuation
        self.last_activate = t

    def split(self): # 只有激活区间需要分裂
        mid_concept = Concept('mid')
        new_path1 = Path(self.start, mid_concept.id,self.last_activate,self.attenuation/2,self.deepth)
        new_path2 = Path(mid_concept.id, self.end,self.last_activate,self.attenuation/2,self.deepth+1)
        return new_path1,new_path2,mid_concept

    def can_activate(self,t): # 抽象概念路径激活函数 取消概率观点，直接省略低系数路径 参考最长记忆长度 回忆的时候确认
        lasta =  self.last_activate
        delt = t - lasta
        s =  10/delt
        return s>3

# 迭代计算系数。。好难，淦
full_paths = []
def get_final_full_path(start_path, all_paths):
    for path in all_paths:
        if path.start == start_path.end:




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
    newpath = Path(start.id,a.id,t)
    paths.append(newpath)

    # 输入b 基于原先路径生成新路径 并增强公用路径
    t += 1
    newpaths = []
    newpaths.append(Path(start.id,b.id,t))
    for path in paths:
        if path.can_activate(t):
            new_path1,new_path2,mid_concept = path.split()
            new_path1.activate(t)
            newpaths.append(Path(mid_concept.id, b.id,t,deepth=path.deepth+1))
            newpaths.append(new_path1)
            newpaths.append(new_path2)
    for path in newpaths:
        print(path.attenuation,NEURON_DICT[path.start],NEURON_DICT[path.end],path.deepth)



# 回忆测试  从入口计算所有到末端的路径系数

    for path in newpaths:




# 迭代
# 疲劳

# 短期记忆后测试长期回忆
# 互斥计算：各自路径都独立计算，最后比较谁强度最高

# 连接本来就存在，只是点亮了罢了

# 拆分逻辑不太对，不符合b《a的问题，原因是in-b 重复计算了 三角旗模型还要优化


# 记忆abcd # 实验需不需要start节点
if __name__ == '__main__':
    memory()

