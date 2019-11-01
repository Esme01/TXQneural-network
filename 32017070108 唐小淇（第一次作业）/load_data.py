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

for i in range(5):
    print("第", i+1, "个样本标签")
    digit = training_data[i][0].reshape(28, 28)
    # [1][0]是什么意思？第二个图形的第一项（样本）
    print(training_data[i][1])
    print(np.argmax(training_data[i][1]))
    # np.argmax()输出这一行最大值的下标


    # 打印标签
    plt.imshow(digit, cmap=plt.cm.binary)
    plt.show()
    # print(training_data[0])
