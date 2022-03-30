# Монте-Карло (показательный)

import random
import numpy

import main

n = main.n


def indicative_1():
    lt = list()
    for i in range(n):
        x = -numpy.log(random.uniform(0, 1)) / 1.5
        if 1 <= x <= 4:
            lt.append((x ** 2) / 1.5)

    return 'Показательный метод', round(sum(lt) / n, 4)
