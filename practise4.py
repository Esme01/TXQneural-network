import math
import numpy as np


def sigmoid(z):
    return 1/(1+pow(math.e, -z))


class Network():
    def __init__(self, sizes):
        self.sizes = sizes
        w_list = []
        for i in range(len(sizes)-1):
            w_list.append([np.random.randn(sizes[i+1], sizes[i])])

        self.n = n
        self.m = m
        self.weight = np.random.randn(m, n)
        self.biase = np.random.randn(m, 1)

    def __call__(self, x):
        return sigmoid(np.matmul(self.weight, x)+self.biase)
