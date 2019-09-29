import math
# 输入的x是一个数


def sigmoid(z):
    return 1/(1+pow(math.e, -z))


class Network():
    def __init__(self):
        self.weight = 1
        self.biase = 2

    def y(self, x):
        return sigmoid(self.weight*x+self.biase)
    # 不要忘了self


net = Network()
# python创建新对象不需要new，java有new
print(net.y(3))
