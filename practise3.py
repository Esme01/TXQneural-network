import math
import numpy as np


def sigmoid(z):
    return 1/(1+pow(math.e, -z))


class Network():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.weight = np.random.randn(m, n)
        self.biase = np.random.randn(m, 1)

    def __call__(self, x):
        return sigmoid(np.matmul(self.weight, x)+self.biase)


layer1 = Network(5, 3)
layer2 = Network(3, 1)
output = layer2(layer1([[1], [2], [3], [4], [5]]))
# 第一层输出是第二层的输入
# 不用y,用call
print(output)