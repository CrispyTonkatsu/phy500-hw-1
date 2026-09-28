import numpy as np

import utils as ut


def f(x, y):
    return (1 - x) ** 2 + 100 * (y - x**2) ** 2


def f_x(x, y):
    return -400 * x * (-(x**2) + y) + 2 * x - 2


def f_y(x, y):
    return -200 * x**2 + 200 * y


x = np.linspace(-10, 10)
y = np.linspace(-10, 10)

descent_start = [10, 10]

fig = ut.create_plot(
    "Rosenbrock Valley",
    x,
    y,
    f,
    f_x,
    f_y,
    descent_start,
    learn_rate=0.00001,
)

fig.show()
