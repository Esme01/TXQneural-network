def generator(n):
    i = 0
    while i < n:
        yield i
        i = i+1

for i in generator(10):
    print(i)

