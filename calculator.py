import numpy as np
import plotly.graph_objects as go
import sympy as sp

x, y = sp.symbols("x y")
f = (1 - x) ** 2 + 100 * (y - x**2) ** 2

f_x = sp.diff(f, x)
f_y = sp.diff(f, y)

solutions = sp.solve((f_x, f_y), (x, y))

x = np.linspace(-10, 10)
y = np.linspace(-10, 10)


X, Y = np.meshgrid(x, y)
Z = (1 - X) ** 2 + 100 * (Y - X**2) ** 2

surface = go.Surface(x=X, y=Y, z=Z, opacity=0.7)
go.Figure(surface).show()
