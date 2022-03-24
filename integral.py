import math
import random

n = 1000


def integral_1() -> float:

    xMin, xMax, yMin, yMax = 1, 4, 0, 0.25
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

    xMin, xMax, yMin, yMax = 1, 4, 0, 0.2
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
    xMin, xMax, yMin, yMax = 1, 4, 0, 0.15
    s = (xMax - xMin) * (yMax - yMin)
    below = 0
    for i in range(n):
        x = random.uniform(a=xMin, b=xMax)
        y = random.uniform(a=yMin, b=yMax)
        if y <= math.cos(x) * math.e ** (-1.5 * x):
            below += 1
    evaluationOfTheIntegral = below / n * s
    return evaluationOfTheIntegral
