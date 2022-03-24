import math as m
import random as r

if __name__ == '__main__':

    n = 1000
    xMin, xMax, yMin, yMax = 1, 4, 0, 0.25

    s = (xMax - xMin) * (yMax - yMin)

    below = 0
    for i in range(n):
        x = r.uniform(a=xMin, b=xMax)
        y = r.uniform(a=yMin, b=yMax)
        if y <= (x ** 2) * (m.e ** (-1.5 * x)):
            below += 1

    evaluationOfTheIntegral = below / n * s
    print('I =', round(number=evaluationOfTheIntegral, ndigits=4))

# comment