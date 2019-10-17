def generator(n):
    i = 0
    while i<n:
        yield i
        i = i+1
l = list(generator(10))
print(l)
# zip是一个generator类型，必须用list才能把数据放到内存
