#метод трапеций

import numpy as np


def trapezoid_1():
    a = 1
    b = 4
    n = 50
    h = (b - a) / n

    y = list()
    for i in range(n):
        x = a + i * h
        f = (x ** 2) * (np.e ** (-1.5 * x))
        y.append(f)

    trap = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return 'Метод трапеций (узлов {})'.format(n), round(trap, 4)
