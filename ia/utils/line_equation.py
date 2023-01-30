import matplotlib.pyplot as plt
import math


def line_equation(m, x, p=3):
    return m * x + p

plt.axhline(y = 0, color = 'red')
plt.axvline(x = 0, color = 'red')
plt.axline((-1, line_equation(-2, -1)), (1, line_equation(-2, 1)))
plt.scatter([0,0,1,1], [0,1,0,1])
plt.show()