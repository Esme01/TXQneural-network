import math
import numpy as np
# 输入的x是列向量


def sigmoid(z):
    return 1/(1+pow(math.e, -z))


class Network():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.weight = np.random.randn(m, n)
        # ？？？
        self.biase = np.random.randn(m, 1)

    def y(self, x):
        return sigmoid(np.matmul(self.weight, x)+self.biase)
# 矩阵的乘积，“*”就是对应位置相乘，dot也可以表示矩阵相乘
# n输入m输出
# 已经做了一层神经元


net = Network(5, 3)
print(net.y([[1], [2], [3], [4], [5]]))
# x必须是1行m列
print(net.weight)
print(net.biase)