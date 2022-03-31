# метод прямоугольников

import numpy as np

a = 1
b = 4
n = 50
h = (b - a) / n


def rectangle_1() -> tuple[str, float]:
    f = list()
    for i in range(n):
        x = a + (i + 1 - h) * h
        y = (x ** 2) * (np.e ** (-1.5 * x))
        f.append(y)
    s = h * sum(f)
    return 'Метод прямоугольников (узлов {})'.format(n), round(s, 4)


def rectangle_2() -> tuple[str, float]:
    f = list()
    for i in range(n):
        x = a + (i + 1 - h) * h
        y = np.sin(x) * (np.e ** (-1.5 * x))
        f.append(y)
    s = h * sum(f)
    return 'Метод прямоугольников (узлов {})'.format(n), round(s, 4)


def rectangle_3() -> tuple[str, float]:
    f = list()
    for i in range(n):
        x = a + (i + 1 - h) * h
        y = np.cos(x) * (np.e ** (-1.5 * x))
        f.append(y)
    s = h * sum(f)
    return 'Метод прямоугольников (узлов {})'.format(n), round(s, 4)
