import math
import numpy as np
import matplotlib.pyplot as plt
import integral

n = integral.n
a = 1
b = 4


def graph_1():
    y = lambda x: (x ** 2) * (math.e ** (-1.5 * x))
    x = np.linspace(a, b, n)
    plt.plot(x, y(x))
    plt.show()


def graph_2():
    y = lambda x: math.sin(x) * (math.e ** (-1.5 * x))
    x = np.linspace(a, b, n)
    plt.plot(x, y(x))
    plt.show()


def graph_3():
    y = lambda x: math.cos(x) * (math.e ** (-1.5 * x))
    x = np.linspace(a, b, n)
    plt.plot(x, y(x))
    plt.show()
