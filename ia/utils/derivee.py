import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    return 1/math.sqrt(2*math.pi) * (math.e**(-0.5 * x**2))

def pentes(x, y):
    p = []
    for i in range(len(x) - 1):
        pente = (y[i+1]-y[i])/(x[i+1]-x[i])
        p.append(pente)
    p.append(p[len(p)-1])
    return p

x = np.linspace(-5.0, 5.0, num=10000)
y = np.array(list(map(f, x)))
plt.plot(x, y, label="function", c="blue")
plt.plot(x, pentes(x, y), label="derivee", c="red")
plt.plot(x, pentes(x, pentes(x, y)), label="derivee", c="orange")
plt.axhline(y = 0, color = 'green')
plt.show()