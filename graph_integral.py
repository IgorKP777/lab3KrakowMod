import numpy as np
import matplotlib.pyplot as plt
import main

n = main.n
a = main.a
b = main.b


def graph_1():
    y = lambda x: (x ** 2) * (np.e ** (-1.5 * x))
    x = np.linspace(a, b, n)
    plt.plot(x, y(x))
    plt.show()


def graph_2():
    y = lambda x: np.sin(x) * (np.e ** (-1.5 * x))
    x = np.linspace(a, b, n)
    plt.plot(x, y(x))
    plt.show()


def graph_3():
    y = lambda x: np.cos(x) * (np.e ** (-1.5 * x))
    x = np.linspace(a, b, n)
    plt.plot(x, y(x))
    plt.show()
