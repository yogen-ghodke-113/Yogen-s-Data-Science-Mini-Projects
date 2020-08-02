from numpy.random import randn


def calc(num):
    y = randn(num)
    count = 0
    for x in y:
        if -1 < x < 1:
            count += 1
    return count / num


li = []
for x in range(10):
    l = []
    l.append(calc(5))
    l.append(calc(10))
    l.append(calc(100))
    l.append(calc(1000))
    l.append(calc(100000))
    l.append(calc(1000000))
    li.append(l.copy())
    l.clear()

for x in li:
    j = list(map(lambda z: z * 100, x))
    print(j)
