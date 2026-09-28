import numpy as np

import utils as ut


def f(x, y):
    return 2 - np.exp(-(x**4) - y**2) - (1 / (x**2 + y**4 + 1))


def f_x(x, y):
    return 4 * x**3 * np.exp(-(x**4) - y**2) + 2 * x / (x**2 + y**4 + 1) ** 2


def f_y(x, y):
    return 4 * y**3 / (x**2 + y**4 + 1) ** 2 + 2 * y * np.exp(-(x**4) - y**2)


x = np.linspace(-4, 4)
y = np.linspace(-4, 4)

descent_start = [-2, -2]

fig = ut.create_plot(
    "Crater Thing",
    x,
    y,
    f,
    f_x,
    f_y,
    descent_start,
    hard_crit_points=[
        (
            0,
            0,
            f(0, 0),
            "Critical point",
        )
    ],
)

fig.show()
