#через первообразную (аналитический метод)

import numpy as np


def primitive_1() -> tuple[str, float]:
    y = lambda x: -np.e ** (-1.5 * x) * (((x ** 2) / 1.5) + ((2 * x) / (1.5 ** 2)) + (2 / (1.5 ** 3)))
    return 'Аналитический метод', round(y(4) - y(1), 4)


def primitive_2() -> tuple[str, float]:
    y = lambda x: (-(np.e ** (-1.5 * x)) / ((1.5 ** 2) + 1)) * (1.5 * np.sin(x) + np.cos(x))
    return 'Аналитический метод', round(y(4) - y(1), 4)


def primitive_3() -> tuple[str, float]:
    y = lambda x: ((np.e ** (-1.5 * x)) / ((1.5 ** 2) + 1)) * (np.sin(x) - 1.5 * np.cos(x))
    return 'Аналитический метод', round(y(4) - y(1), 4)
