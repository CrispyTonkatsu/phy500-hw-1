import numpy as np
import plotly.graph_objects as go
import sympy as sp

x, y = sp.symbols("x y")
f = 2 - sp.exp(-(x**4) - y**2) - (1 / (x**2 + y**4 + 1))

hessian = sp.hessian(f, (x, y))

ev_hessian = sp.Subs(hessian, (x, y), (0, 0))
np_hessian = sp.matrix2numpy(ev_hessian)

eigvals = np.linalg.eigvals(np_hessian)
print(eigvals)
