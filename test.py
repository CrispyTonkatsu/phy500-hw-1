import marimo

__generated_with = "0.11.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go

    return go, mo, np


@app.cell
def _(mo):
    mo.md(
        r"""
        # Multivariable Calculus: Gradient Fields & Surfaces

        Let our scalar function be defined as:
        $$f(x, y) = \sin(x)\cos(y)$$

        To find the direction of steepest ascent, we compute its analytical gradient vector field $\nabla f(x, y)$:
        $$\nabla f(x, y) = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right) = (\cos(x)\cos(y), -\sin(x)\sin(y))$$

        Below is the static visualization optimized for reliable PDF printing and homework submission.
        """
    )


@app.cell
def _(go, mo, np):
    # 1. Define grid and test function
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)

    # 2. Surface trace
    surface = go.Surface(
        z=Z,
        x=X,
        y=Y,
        colorscale="Viridis",
        opacity=0.75,
        name="f(x, y)",
    )

    # 3. Vector field calculations (Gradient)
    U = np.cos(X) * np.cos(Y)
    V = -np.sin(X) * np.sin(Y)
    W = np.zeros_like(U)

    step = 10
    xs = X[::step, ::step].flatten()
    ys = Y[::step, ::step].flatten()
    zs = -1.5 * np.ones_like(xs)  # Positioned flat on the floor
    us = U[::step, ::step].flatten()
    vs = V[::step, ::step].flatten()
    ws = W[::step, ::step].flatten()

    cones = go.Cone(
        x=xs,
        y=ys,
        z=zs,
        u=us,
        v=vs,
        w=ws,
        sizemode="absolute",
        sizeref=0.15,
        colorscale="Reds",
        showscale=False,
        name="Gradient Field",
    )

    # 4. Assemble figure and layouts
    fig = go.Figure(data=[surface, cones])

    fig = fig.update_traces(
        contours_z={
            "show": True,
            "usecolormap": True,
            "project_z": True,
            "highlightcolor": "limegreen",
        },
        selector={"type": "surface"},
    )

    fig.update_layout(
        title="Calculus Homework Static Model",
        scene={
            "xaxis_title": "X Axis",
            "yaxis_title": "Y Axis",
            "zaxis_title": "Z Axis",
            "aspectratio": {"x": 1, "y": 1, "z": 0.7},
        },
        width=850,
        height=650,
    )

    # 5. Compile to static image bytes using kaleido for print compatibility
    img_bytes = fig.to_image(format="png", scale=2)

    # Display the static image through marimo
    mo.image(src=img_bytes, width=800)


if __name__ == "__main__":
    app.run()
