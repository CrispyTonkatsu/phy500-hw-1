import numpy as np

import utils as ut


def f(x, y):
    return (x**2 - 1) ** 2 + y**2


def f_x(x, y):
    return 4 * x**3 - 4 * x


def f_y(x, y):
    return 2 * y


x = np.linspace(-2, 2)
y = np.linspace(-2, 2)

descent_start = [-2, -2]

fig = ut.create_plot("Quadratic", x, y, f, f_x, f_y, descent_start)

fig.show()
