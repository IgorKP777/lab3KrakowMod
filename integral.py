#метод Монте-Карло

import math
import random

import main

n = main.n
xMin, xMax, yMin, yMax = main.a, main.b, 0, 0.25


def integral_1() -> float:
    s = (xMax - xMin) * (yMax - yMin)
    below = 0
    for i in range(n):
        x = random.uniform(a=xMin, b=xMax)
        y = random.uniform(a=yMin, b=yMax)
        if y <= (x ** 2) * (math.e ** (-1.5 * x)):
            below += 1
    evaluationOfTheIntegral = below / n * s
    return evaluationOfTheIntegral


def integral_2() -> float:
    s = (xMax - xMin) * (yMax - yMin)
    below = 0
    for i in range(n):
        x = random.uniform(a=xMin, b=xMax)
        y = random.uniform(a=yMin, b=yMax)
        if y <= math.sin(x) * math.e ** (-1.5 * x):
            below += 1
    evaluationOfTheIntegral = below / n * s
    return evaluationOfTheIntegral


def integral_3() -> float:
    s = (xMax - xMin) * (yMax - yMin)
    below = 0
    for i in range(n):
        x = random.uniform(a=xMin, b=xMax)
        y = random.uniform(a=yMin, b=yMax)
        if y <= math.cos(x) * math.e ** (-1.5 * x):
            below += 1
    evaluationOfTheIntegral = below / n * s
    return evaluationOfTheIntegral
