import numpy as np
import plotly.graph_objects as go
import sympy as sp

x, y = sp.symbols("x y")
f = (x**2 + y - 11) ** 2 + (x + y**2 - 7) ** 2

f_x = sp.diff(f, x)
f_y = sp.diff(f, y)

hessian = sp.hessian(f, (x, y))

solutions = sp.solve((f_x, f_y), (x, y))

for index, (s_x, s_y) in enumerate(solutions):
    print(f"Solution for {index}")
    ev_hessian = hessian.subs(
        {
            x: s_x.evalf(),
            y: s_y.evalf(),
        }
    )

    sp.print_latex(ev_hessian.eigenvals())
