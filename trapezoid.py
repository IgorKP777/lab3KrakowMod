# метод трапеций

import numpy as np

a = 1
b = 4
n = 50
h = (b - a) / n


def trapezoid_1() -> tuple[str, float]:
    y = list()
    for i in range(n):
        x = a + i * h
        f = (x ** 2) * (np.e ** (-1.5 * x))
        y.append(f)

    first, *lt, last = y
    trap = (h / 2) * (first + 2 * sum(lt) + last)
    return f'Метод трапеций (узлов {n})', round(trap, 4)


def trapezoid_2() -> tuple[str, float]:
    y = list()
    for i in range(n):
        x = a + i * h
        f = np.sin(x) * (np.e ** (-1.5 * x))
        y.append(f)

    first, *lt, last = y
    trap = (h / 2) * (first + 2 * sum(lt) + last)
    return f'Метод трапеций (узлов {n})', round(trap, 4)


def trapezoid_3() -> tuple[str, float]:
    y = list()
    for i in range(n):
        x = a + i * h
        f = np.cos(x) * (np.e ** (-1.5 * x))
        y.append(f)

    first, *lt, last = y
    trap = (h / 2) * (first + 2 * sum(lt) + last)
    return f'Метод трапеций (узлов {n})', round(trap, 4)
