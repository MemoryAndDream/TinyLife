# -*- coding: utf-8 -*-
"""
Description :
date：          2023/3/27
"""
import numpy as np
import random
import os
import datetime

DEFAULT_BIAS = -1 # 随便想的 先试试


def bs(x):
    # 阶梯激活函数 反正我也不算梯度

    return 1 if x>0 else 0

 


def get_bool(x):

    return x == 1 # 等于条件在input全为0时生效


class Neuron:
    def __init__(self, weights, bias=DEFAULT_BIAS):
        self.weights = weights
        self.bias = bias  # 偏置项 模拟阈值
        self.active = True
        self.last_activate = 0 # 多神经元抽象没有疲劳

    def response(self, inputs):
        # 加权输入，加入偏置，然后使用激活函数
        total = np.dot(self.weights, inputs) + self.bias  # dot点乘，2*0+1*3+4
        return bs(total)


class Organ():  # 器官组织 这个版本的先一个个手写
    def __init__(self,name=''):
        self.neurons = []
        self.inputs = None
        self.outputs = []
        self.name = name

    def response(self, inputs):
        self.outputs = []
        for neuron in self.neurons:
            self.outputs.append(neuron.response(inputs))
        return self.outputs


class Mind:

    def __init__(self):
        self.gen_eyes()
        self.gen_dirt()
        self.gen_stomach()
        self.gen_tail()
        self.gen_skin()
        self.gen_stomach()

    def gen_eyes(self):
        eyes = Organ('eyes')
        eyes.neurons.append(Neuron(np.array([1,-1,])))
        eyes.neurons.append(Neuron(np.array([-1,1,])))
        eyes.neurons.append(Neuron(np.array([1,1,])))
        self.eyes = eyes

    def gen_tail(self): # turn left, forward, turn right
        tail = Organ()
        tail.neurons.append(Neuron(np.array([2, 0, 0, 1])))
        tail.neurons.append(Neuron(np.array([0, 0, 20, -20])))
        tail.neurons.append(Neuron(np.array([0, 2, 0, 1])))
        self.tail = tail


    def gen_dirt(self): # 向左转还是向右转 预测进化结果应该是1 -1
        '概念：左/右'



    def gen_stomach(self):
        pass

    def gen_skin(self): # 边界检测
        '概念：嗷'
        skin = Organ()
        weights = np.array([1,])
        skin.neurons.append(Neuron(weights.copy()))
        self.skin = skin

    def response(self, inputs,skin_input):
        eye_feel = self.eyes.response(inputs)
        skin_feel = self.skin.response(skin_input)
        print(eye_feel, skin_feel)
        turn_left, forward, turn_right = self.tail.response(eye_feel+skin_feel)
        print(get_bool(turn_left), get_bool(forward), get_bool(turn_right))
        return get_bool(turn_left), get_bool(forward), get_bool(turn_right)

    def mutate(self):  # 随机突变
        for org in [self.eyes,self.skin,self.tail]:
            for neuron in org.neurons:
                for i in range(len(neuron.weights)):
                    neuron.weights[i] = random.choice([10,1, 0,-1,-10])

    # def mutate2(self, mutate_rate=5):  # 遗传突变
    #     #     # h_value = random.choice([self.h1.weights,self.h2.weights ,self.h3.weights ,self.h4.weights ,self.h5.weights ,self.h6.weights ,self.h7.weights ,self.h8.weights])
    #     #
    #     #     # h_value[random.choice(range(8))]  += random.choice([1,-1])  # 不知道这么搞好还是随机好？要避免陷入局部最小 所以先随机瞎j8突变
    #     #     weights = [self.h1.weights, self.h2.weights, self.h3.weights, self.h4.weights, self.h5.weights, self.h6.weights,
    #     #                self.h7.weights, self.h8.weights, self.o1.weights, self.o2.weights, self.o3.weights, self.o4.weights]
    #     #     for weight in weights:
    #     #         for i in range(self.input_count):
    #     #             weight[i] = weight[i] + random.randint(-mutate_rate, mutate_rate)
    #     #
    #     # def mutate3(self):  # 遗传突变
    #     #     # h_value = random.choice([self.h1.weights,self.h2.weights ,self.h3.weights ,self.h4.weights ,self.h5.weights ,self.h6.weights ,self.h7.weights ,self.h8.weights])
    #     #
    #     #     # h_value[random.choice(range(8))]  += random.choice([1,-1])  # 不知道这么搞好还是随机好？要避免陷入局部最小 所以先随机瞎j8突变
    #     #     weights = [self.h1.weights, self.h2.weights, self.h3.weights, self.h4.weights, self.h5.weights, self.h6.weights,
    #     #                self.h7.weights, self.h8.weights, self.o1.weights, self.o2.weights, self.o3.weights, self.o4.weights]
    #     #     for weight in weights:
    #     #         for i in range(self.input_count):
    #     #             weight[i] = weight[i] * random.uniform(0.8, 1.2)

    def save(self, name, age, grave_path=None):
        print('保存')
        if not grave_path:
            grave_path = 'data/grave/%s' % datetime.datetime.now().strftime('%Y%m%d%H')
        if not os.path.exists(grave_path):
            os.mkdir(grave_path)
        file_path = grave_path + '/' + name + str(age) + '.npz'
        weights = []
        for org in [self.eyes,self.skin,self.tail]:
            for neuron in org.neurons:
                weights.extend(neuron.weights)
        np.savez(file_path, weights)


    def load(self, file_path):
        with np.load(file_path) as f:
            load_weights = f[
                'arr_0']
        i = 0
        for org in [self.eyes, self.skin, self.tail]:
            for neuron in org.neurons:
                l = len(neuron.weights)
                neuron.weights = load_weights[i:i+l]
                i += l



    def show(self):
        for org in [self.eyes,self.skin,self.tail]:
            print(org.name)
            for neuron in org.neurons:
                print(neuron.weights)



if __name__ == '__main__':
    mind = Mind()
    # mind.mutate()
    # mind.show()
    print(mind.response([11,0], [0]))
    # mind.load(r'E:\github\py3\TinyLife\data\grave\2023042316\1682238946943400.npz')
