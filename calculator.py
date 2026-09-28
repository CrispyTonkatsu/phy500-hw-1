import numpy as np
import plotly.graph_objects as go
import sympy as sp

x, y = sp.symbols("x y")
f = 2 - sp.exp(-(x**4) - y**2) - (1 / (x**2 + y**4 + 1))

f_x = sp.diff(f, x)
f_y = sp.diff(f, y)

print(f_y)

hessian = sp.hessian(f, (x, y))

ev_hessian = hessian.subs({x: 0, y: 0})
np_hessian = sp.matrix2numpy(ev_hessian, dtype=float)

eigen_values = np.linalg.eigvalsh(np_hessian)
