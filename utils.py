import numpy as np
import plotly.graph_objects as go


def gradient_descent(start, learn_rate, f_grad, slope_target=0.05):
    x = start
    x_seq = [x.copy()]
    grad = np.array(f_grad(x[0], x[1]))

    while np.dot(grad, grad) > slope_target**2:
        x = x - learn_rate * grad
        grad = np.array(f_grad(x[0], x[1]))
        x_seq.append(x.copy())

    return x_seq


def plot_function(title, X, Y, Z, U, V, crit_points, f, descent_path):
    surface = go.Surface(
        x=X,
        y=Y,
        z=Z,
        colorscale="Viridis",
        opacity=0.7,
        colorbar={"thickness": 15, "len": 0.6},
        contours={
            "z": {
                "show": True,
                "size": 1.5,
            },
        },
    )

    cx = [p[0] for p in crit_points]
    cy = [p[1] for p in crit_points]
    cz = [p[2] for p in crit_points]

    points_trace = go.Scatter3d(
        x=cx,
        y=cy,
        z=cz,
        mode="markers+text",
        marker={"size": 4, "color": "red", "symbol": "circle"},
        textposition="top center",
        textfont={"color": "white", "size": 12},
        name="Critical Points",
    )

    z_floor = np.full_like(X, np.min(Z))
    w_zeros = np.zeros_like(U)

    skip = (slice(None, None, 4), slice(None, None, 4))

    vectors = go.Cone(
        x=X[skip].flatten(),
        y=Y[skip].flatten(),
        z=z_floor[skip].flatten(),
        u=U[skip].flatten(),
        v=V[skip].flatten(),
        w=w_zeros[skip].flatten(),
        sizemode="scaled",
        sizeref=0.6,
        anchor="tail",
        colorscale="Inferno",
        showscale=False,
    )

    px = [p[0] for p in descent_path]
    py = [p[1] for p in descent_path]
    pz = [f(p[0], p[1]) for p in descent_path]

    descent_path_trace = go.Scatter3d(
        x=px,
        y=py,
        z=pz,
        mode="lines+markers",
        marker={"size": 4, "color": "orange", "symbol": "diamond"},
        line={"color": "orange", "width": 5},
        name="Gradient Descent",
    )

    fig = go.Figure([surface, points_trace, vectors, descent_path_trace])

    fig.update_layout(
        title={"text": title, "font": {"size": 16}},
        width=720,
        height=720,
    )

    return fig


def create_plot(
    title,
    x,
    y,
    f,
    f_x,
    f_y,
    crit_points,
    descent_start,
    learn_rate=0.05,
    slope_target=0.05,
):
    def f_grad(x, y):
        return [f_x(x, y), f_y(x, y)]

    X, Y = np.meshgrid(x, y)
    Z = f(Y, X)

    U = f_x(X, Y)
    V = f_y(X, Y)

    descent_path = gradient_descent(descent_start, learn_rate, f_grad, slope_target)

    return plot_function(title, X, Y, Z, U, V, crit_points, f, descent_path)
