# -*- coding: utf-8 -*-
"""
Description : 测试没有阈值的神经元组合是否可以实现先增后减效果(太饿太饱都痛苦)
date：          2023/4/21
"""
import numpy as np

def sigmoid(x): # 激活函数加入非线性因素
  # 我们的激活函数: f(x) = 1 / (1 + e^(-x))
  return max(max(0,x),6)


from matplotlib import pyplot as plt
import numpy as np
import math
x=list(np.arange(-5,5,0.01))#此处可调整自变量取值范围，以便选择合适的观察尺度
y=[]
for i in range(len(x)):
    n = x[i]
    y.append(sigmoid(n))
plt.plot(x,y)
plt.show()
