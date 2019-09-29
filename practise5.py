from network1 import *
import numpy as np
n = Network([5, 4, 3, 2, 1])
print(n.weights)
print("--------------")
print(n.biases)
print("--------------")
Y = n.feedforward([[1], [2], [3], [4], [5]])
print(Y)