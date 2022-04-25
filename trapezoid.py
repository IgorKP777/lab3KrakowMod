# метод трапеций

import numpy as np


a = 1
b = 4
n = 50
h = (b - a) / n


def trapezoid_1():
    y = list()
    for i in range(n):
        x = a + i * h
        f = (x ** 2) * (np.e ** (-1.5 * x))
        y.append(f)

    first, *lt, last = y
    trap1 = (h / 2) * (first + 2 * sum(lt) + last)
    trap = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return 'Метод трапеций (узлов {})'.format(n), round(trap, 4)


def trapezoid_2():
    y = list()
    for i in range(n):
        x = a + i * h
        f = np.sin(x) * (np.e ** (-1.5 * x))
        y.append(f)

    trap = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return 'Метод трапеций (узлов {})'.format(n), round(trap, 4)


def trapezoid_3():
    y = list()
    for i in range(n):
        x = a + i * h
        f = np.cos(x) * (np.e ** (-1.5 * x))
        y.append(f)

    trap = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return 'Метод трапеций (узлов {})'.format(n), round(trap, 4)
