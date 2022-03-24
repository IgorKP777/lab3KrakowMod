import math as m
import random as r
import art

n = 1000


def integral_1():

    xMin, xMax, yMin, yMax = 1, 4, 0, 0.25

    s = (xMax - xMin) * (yMax - yMin)

    below = 0
    for i in range(n):
        x = r.uniform(a=xMin, b=xMax)
        y = r.uniform(a=yMin, b=yMax)
        if y <= (x ** 2) * (m.e ** (-1.5 * x)):
            below += 1

    evaluationOfTheIntegral = below / n * s
    print(art.text2art('I = ' + str(round(number=evaluationOfTheIntegral, ndigits=4)), 'block'))


def integral_2():
    pass


def integral_3():
    pass


if __name__ == '__main__':
    integral_number = int()
    try:
        integral_number = int(input('введите номер интеграла '))
    except ValueError:
        print('введите число')
        exit(-2)

    if 1 <= integral_number <= 3:
        if integral_number == 1:
            integral_1()
        if integral_number == 2:
            integral_2()
        if integral_number == 3:
            integral_3()
    else:
        print('введите номер интегралла от 1 до 3')
    pass
