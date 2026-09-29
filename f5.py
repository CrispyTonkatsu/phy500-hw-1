import numpy as np

import utils as ut


def f(x, y):
    return (x**2 + y - 11) ** 2 + (x + y**2 - 7) ** 2


def f_x(x, y):
    return 4 * x * (x**2 + y - 11) + 2 * x + 2 * y**2 - 14


def f_y(x, y):
    return 2 * x**2 + 4 * y * (x + y**2 - 7) + 2 * y - 22


x = np.linspace(-10, 10)
y = np.linspace(-10, 10)

descent_start = [10, 10]

fig = ut.create_plot(
    "Himmelblaus' Function",
    x,
    y,
    f,
    f_x,
    f_y,
    descent_start,
    learn_rate=0.001,
)

fig.show()
