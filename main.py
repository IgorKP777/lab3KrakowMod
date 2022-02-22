import math as m
import random as r

if __name__ == '__main__':

    n = 1000
    xMin = 1
    xMax = 4
    yMin = 0
    yMax = 0.25

    s = (xMax - xMin) * (yMax - yMin)

    xList =[]
    yList =[]
    below = 0
    for i in range(n):
        xList.append(r.uniform(xMin, xMax))
        yList.append(r.uniform(yMin, yMax))
        if yList[i] <= (xList[i] ** 2) * (m.e ** (-1.5 * xList[i])):
            below += 1

    evaluationOfTheIntegral = below / n * s
    print('I =', round(evaluationOfTheIntegral, 4))
