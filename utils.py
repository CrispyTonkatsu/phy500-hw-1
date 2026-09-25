import numpy as np
import plotly.graph_objects as go


def plot_function(title, X, Y, Z, U, V, crit_points):
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
    labels = [p[3] for p in crit_points]

    points_trace = go.Scatter3d(
        x=cx,
        y=cy,
        z=cz,
        mode="markers+text",
        marker={"size": 8, "color": "red", "symbol": "circle"},
        text=labels,
        textposition="top center",
        textfont={"color": "white", "size": 12},
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

    fig = go.Figure([surface, points_trace, vectors])

    fig.update_layout(
        title={"text": title, "font": {"size": 16}},
        width=720,
        height=720,
    )

    return fig
