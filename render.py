import numpy as np

import utils as ut


def f(x, y):
    return 3 * x**2 + 2 * x * y + 2 * y**2


def f_x(x, y):
    return 6 * x + 2 * y


def f_y(x, y):
    return 2 * x + 4 * y


x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)

descent_start = [10, 10]

fig = ut.create_plot("Quadratic", x, y, f, f_x, f_y, [(0, 0, 0)], descent_start)

fig.show()
