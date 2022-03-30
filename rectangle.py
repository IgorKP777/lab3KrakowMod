import numpy as np

a = 1
b = 4
n = 50
h = (b - a) / n


def rectangle_1():
    f = list()
    for i in range(n):
        x = a + (i + 1 - h) * h
        y = (x ** 2) * (np.e ** (-1.5 * x))
        f.append(y)
    s = h * sum(f)
    return 'Метод прямоугольников', round(s, 4)


print(rectangle_1())
