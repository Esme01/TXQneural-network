import math


def sigmoid(z):
    return 1/(1+pow(math.e,-z))


class Network():
    def __init__(self):
        self.weight = 1
        self.biase = 2

    def y(self, x):
        return sigmoid(self.weight*x+self.biase)


net = Network()
print(net.y(3))
