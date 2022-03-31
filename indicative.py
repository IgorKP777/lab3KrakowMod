# Монте-Карло (показательный закон)
# min 0.4005
# max 0.4892

import random
import numpy

n = 10000


def indicative_1() -> tuple[str, float]:
    lt = list()
    for i in range(n):
        x = -numpy.log(random.random()) / 1.5
        if 1 <= x <= 4:
            lt.append((x ** 2) / 1.5)
    return 'Монте-Карло (показательный закон)', round(sum(lt) / n, 4)


def indicative_2() -> tuple[str, float]:
    lt = list()
    for i in range(n):
        x = -numpy.log(random.uniform(0, 1)) / 1.5
        if 1 <= x <= 4:
            lt.append((x ** 2) / 1.5)
    return 'Монте-Карло (показательный закон)', round(sum(lt) / n, 4)


def indicative_3() -> tuple[str, float]:
    lt = list()
    for i in range(n):
        x = -numpy.log(random.uniform(0, 1)) / 1.5
        if 1 <= x <= 4:
            lt.append((x ** 2) / 1.5)
    return 'Монте-Карло (показательный закон)', round(sum(lt) / n, 4)


lt = []
for _ in range(20000):
    lt.append(indicative_1()[1])
print(min(lt))
print(max(lt))
