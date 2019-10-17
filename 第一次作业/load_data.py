import MNST_load
import matplotlib.pyplot as plt
import numpy as np
training_data, validation_data, test_data = MNST_load.load_data_wrapper()

# print(type(training_data))
training_data = list(training_data)
# 为什么要变成list？traing_data是zip类型（“平行走”的变量），zip没有“len”,是"generator"
test_data = list(test_data)
print(len(training_data))
print(len(test_data))
digit = training_data[1][0].reshape(28, 28)
plt.imshow(digit, cmap=plt.cm)
plt.show()
