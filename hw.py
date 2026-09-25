import marimo

__generated_with = "0.11.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go

    mo.latex(filename="macros.tex")

    return go, mo, np


@app.cell
def _(mo):
    mo.md(
        r"""
        # Gradient Descent Optimization and Graphics!
        """
    )


@app.cell
def _(mo):
    mo.md(r"""
    ## Rotated Anisotropic Quadratic
    $$
    z = f(x, y) = 3x^2 + 2xy + 2y^2
    $$

    ### Gradient
    $$
    \grad f(x,y) =
    \begin{bmatrix}
    \end{bmatrix}
    $$

    ### Hessian
    ### Critical Points
    ### SOC for optimality
    """)


if __name__ == "__main__":
    app.run()
