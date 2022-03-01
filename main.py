import math as m
import random as r

if __name__ == '__main__':

    n = 1000
    xMin = 1
    xMax = 4
    yMin = 0
    yMax = 0.25

    s = (xMax - xMin) * (yMax - yMin)

    below = 0
    for i in range(n):
        x = r.uniform(xMin, xMax)
        y = r.uniform(yMin, yMax)
        if y <= (x ** 2) * (m.e ** (-1.5 * x)):
            below += 1

    evaluationOfTheIntegral = below / n * s
    print('I =', round(evaluationOfTheIntegral, 4))
