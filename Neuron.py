# import math
# import numpy as np
# # 一个神经元，N个输入
# # 用numpy产生均值为0，方差为1的高斯分布
#
#
# def sigmoid(x):
#     # our activation function: f(x) = 1 / (1 * e^(-x))
#     return 1 / (1 + np.exp(-x))
#
#
# class Neuron( ):
#     def __init__(self, weights, bias):
#         self.weights = weights
#         self.bias = bias
#
#     def feedforward(self, inputs):
#         # weight inputs, add bias, then use the activation function
#         total = np.dot(self.weights, inputs) + self.bias
#         return sigmoid(total)
#
#
# weights = np.array([0, 1])  # w1 = 0, w2 = 1
# bias = 4
# n = Neuron(weights, bias)
#
# # inputs
# x = np.array([2, 3])  # x1 = 2, x2 = 3
# print(n.feedforward(x))  # 0.9990889488055994


#### Libraries
# Standard library
import random

# Third-party libraries
import numpy as np


class Network(object):

    def __init__(self, sizes):
        """The list ``sizes`` contains the number of neurons in the
        respective layers of the network.  For example, if the list
        was [2, 3, 1] then it would be a three-layer network, with the
        first layer containing 2 neurons, the second layer 3 neurons,
        and the third layer 1 neuron.  The biases and weights for the
        network are initialized randomly, using a Gaussian
        distribution with mean 0, and variance 1.  Note that the first
        layer is assumed to be an input layer, and by convention we
        won't set any biases for those neurons, since biases are only
        ever used in computing the outputs from later layers."""
        # 把每个变量的值打印出来
        # 这只是整个代码的一部分，如何打印出来呢？
        self.num_layers = len(sizes)
        print("self.num_layers:")
        print(self.num_layers)
        self.sizes = sizes
        print("self.sizes:")
        print(self.sizes)
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        print("self.biases:")
        print(self.biases)
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
        print("self.weights:")
        print(self.weights)


net = Network([2, 3, 1])
print("_____________________________________________________________")
print("net.sizes:")
print(net.sizes)
print("net.biases:")
print(net.biases)
print("net.num_layers:")
print(net.num_layers)
print("net.weights:")
print(net.weights)

b = [2*e for e in a if e > 2]
print(b)

code = [1, 2, 3, 4]
name = ['zhang', 'chen', 'liu']
d={}
for c,n in zip(code, name):
    d[c] = n
print(d)


