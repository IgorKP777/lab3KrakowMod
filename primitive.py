import numpy as np

y = lambda x: -np.e ** (-1.5 * x) * (((x ** 2) / 1.5) + ((2 * x) / (1.5 ** 2)) + (2 / (1.5 ** 3)))

print(round(y(4) - y(1), 4))
