import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    return 1/math.sqrt(2*math.pi) * (math.e**(-0.5 * x**2))

def pentes(x, f, step=0.01):
    acc = []
    for i in range(len(x)):
        x1 = x[i] - step
        x2 = x[i] + step
        y1 = f(x1)
        y2 = f(x2)
        pente = (y2-y1)/(x2-x1)
        acc.append(pente)
    return acc

x = np.linspace(-5.0, 5.0, num=10000)
y = np.array(list(map(f, x)))
plt.plot(x, y, label="function", c="blue")
plt.plot(x, pentes(x, f), label="derivee", c="red")
plt.axhline(y = 0, color = 'green')
plt.show()