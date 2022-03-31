# метод Монте-Карло

import math
import random


xMin, xMax, yMin, yMax = 1, 4, 0, 0.25
s = (xMax - xMin) * (yMax - yMin)
n = 10000


def integral_1() -> tuple[str, float]:
    below = 0
    for i in range(n):
        x = random.uniform(a=xMin, b=xMax)
        y = random.uniform(a=yMin, b=yMax)
        if y <= (x ** 2) * (math.e ** (-1.5 * x)):
            below += 1
    evaluationOfTheIntegral = below / n * s
    return 'Метод Монте-Карло', round(evaluationOfTheIntegral, 4)


def integral_2() -> tuple[str, float]:
    below = 0
    for i in range(n):
        x = random.uniform(a=xMin, b=xMax)
        y = random.uniform(a=yMin, b=yMax)
        if y <= math.sin(x) * math.e ** (-1.5 * x):
            below += 1
    evaluationOfTheIntegral = below / n * s
    return 'Метод Монте-Карло', round(evaluationOfTheIntegral, 4)


def integral_3() -> tuple[str, float]:
    below = 0
    for i in range(n):
        x = random.uniform(a=xMin, b=xMax)
        y = random.uniform(a=yMin, b=yMax)
        if y <= math.cos(x) * math.e ** (-1.5 * x):
            below += 1
    evaluationOfTheIntegral = below / n * s
    return 'Метод Монте-Карло', round(evaluationOfTheIntegral, 4)
