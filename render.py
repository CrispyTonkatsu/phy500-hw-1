import numpy as np

import utils as ut

x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)

X, Y = np.meshgrid(x, y)
Z = 3 * X**2 + 2 * X * Y + 2 * Y**2

U = 6 * X + 2 * Y
V = 2 * X + 4 * Y

fig = ut.plot_function("Quadratic", X, Y, Z, U, V, [(0, 0, 0, "Local Min")])

fig.show()
