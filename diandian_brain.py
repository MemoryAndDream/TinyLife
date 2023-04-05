# -*- coding: utf-8 -*-
"""
Description :
date：          2023/3/27
"""
import numpy as np
import random
import os
import datetime

def sigmoid(x): # 激活函数加入非线性因素
  # 我们的激活函数: f(x) = 1 / (1 + e^(-x))
  return 1 / (1 + np.exp(-x))

def get_bool(x):
  return x>=0.5

class Neuron:
  def __init__(self, weights, bias):
    self.weights = weights
    self.bias = bias # 偏置项 模拟阈值

  def feedforward(self, inputs):
    # 加权输入，加入偏置，然后使用激活函数
    total = np.dot(self.weights, inputs) + self.bias # dot点乘，2*0+1*3+4
    return sigmoid(total)

class DianDianBrain:

  def __init__(self):
    weights = np.array([1,1,1,1,1,1,1,1]) # 初始化所有神经元权重为1
    bias = 0
    self.input_count = 8

    # 这里是来自前一节的神经元类 后续需要优化成按序号生成一批
    self.h1 = Neuron(weights.copy(), bias)
    self.h2 = Neuron(weights.copy(), bias)
    self.h3 = Neuron(weights.copy(), bias)
    self.h4 = Neuron(weights.copy(), bias)
    self.h5 = Neuron(weights.copy(), bias)
    self.h6 = Neuron(weights.copy(), bias)
    self.h7 = Neuron(weights.copy(), bias)
    self.h8 = Neuron(weights.copy(), bias)
    # self.h9 = Neuron(weights, bias)
    # 神经元数量的进化先放放
    self.o1 = Neuron(weights.copy(), bias)
    self.o2 = Neuron(weights.copy(), bias)
    self.o3 = Neuron(weights.copy(), bias)
    self.o4 = Neuron(weights.copy(), bias)

  def feedforward(self, x):
    out_h1 = self.h1.feedforward(x)
    out_h2 = self.h2.feedforward(x)
    out_h3 = self.h3.feedforward(x)
    out_h4 = self.h4.feedforward(x)
    out_h5 = self.h5.feedforward(x)
    out_h6 = self.h6.feedforward(x)
    out_h7 = self.h7.feedforward(x)
    out_h8 = self.h8.feedforward(x)

    # o1的输入是h1和h2的输出
    input_h = np.array([out_h1,out_h2,out_h3,out_h4,out_h5,out_h6,out_h7,out_h8])
    out_o1 = self.o1.feedforward(input_h)
    out_o2 = self.o2.feedforward(input_h)
    out_o3 = self.o3.feedforward(input_h)
    out_o4 = self.o4.feedforward(input_h)
    return get_bool(out_o1),get_bool(out_o2),get_bool(out_o3),get_bool(out_o4)

  def mutate(self): #突变
    # h_value = random.choice([self.h1.weights,self.h2.weights ,self.h3.weights ,self.h4.weights ,self.h5.weights ,self.h6.weights ,self.h7.weights ,self.h8.weights])

    # h_value[random.choice(range(8))]  += random.choice([1,-1])  # 不知道这么搞好还是随机好？要避免陷入局部最小 所以先随机瞎j8突变
    weights = [self.h1.weights, self.h2.weights, self.h3.weights, self.h4.weights, self.h5.weights, self.h6.weights,
     self.h7.weights, self.h8.weights, self.o1.weights,self.o2.weights,self.o3.weights,self.o4.weights]
    for weight in weights:
      for i in range(self.input_count):
        weight[i] = random.randint(-100,100)

   # 权重暂时定为[-100,100]间的随机数

  def mutate2(self): #小突变
    # h_value = random.choice([self.h1.weights,self.h2.weights ,self.h3.weights ,self.h4.weights ,self.h5.weights ,self.h6.weights ,self.h7.weights ,self.h8.weights])

    # h_value[random.choice(range(8))]  += random.choice([1,-1])  # 不知道这么搞好还是随机好？要避免陷入局部最小 所以先随机瞎j8突变
    weights = [self.h1.weights, self.h2.weights, self.h3.weights, self.h4.weights, self.h5.weights, self.h6.weights,
     self.h7.weights, self.h8.weights, self.o1.weights,self.o2.weights,self.o3.weights,self.o4.weights]
    for weight in weights:
      for i in range(self.input_count):
        weight[i] = weight[i] + random.randint(-10,10)

  def save(self, name, age):
    grave_path = 'data/grave/%s'%datetime.datetime.now().strftime('%Y%m%d%H')
    if not os.path.exists(grave_path):
      os.mkdir(grave_path)
    file_path = grave_path+'/'+ name+'.npz'
    print(name, 'die at: ', age)
    weights = [self.h1.weights, self.h2.weights, self.h3.weights, self.h4.weights, self.h5.weights, self.h6.weights,
     self.h7.weights, self.h8.weights, self.o1.weights,self.o2.weights,self.o3.weights,self.o4.weights]
    np.savez(file_path, weights)

  def load(self,file_path):

    with np.load(file_path) as f:
      self.h1.weights, self.h2.weights, self.h3.weights, self.h4.weights, self.h5.weights, self.h6.weights,\
      self.h7.weights, self.h8.weights, self.o1.weights, self.o2.weights, self.o3.weights, self.o4.weights =f['arr_0']



if __name__ == '__main__':
    diandian_brain = DianDianBrain()
    print(diandian_brain.feedforward( np.array([1,2,1,0,0,0,0,0]) ))
    diandian_brain.mutate()
    for h in [diandian_brain.h1.weights,diandian_brain.h2.weights ,diandian_brain.h3.weights ,diandian_brain.h4.weights ,diandian_brain.h5.weights ,diandian_brain.h6.weights
                              ,diandian_brain.h7.weights ,diandian_brain.h8.weights]:
      print(h)

