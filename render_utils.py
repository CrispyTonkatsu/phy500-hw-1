import numpy as np
import plotly.graph_objects as go


def plot_function(X, Y, Z, title):
    fig = go.Figure(
        data=[
            go.Surface(
                x=X,
                y=Y,
                z=Z,
                colorscale="Viridis",
                opacity=0.9,
                colorbar={"thickness": 15, "len": 0.6},
            )
        ]
    )

    fig.update_layout(
        title={"text": title, "x": 0.5, "font": {"size": 16}},
        scene={
            "xaxis_title": "x",
            "yaxis_title": "y",
            "zaxis_title": "z",
            "camera": {
                "eye": {
                    "x": 1.5,
                    "y": -1.5,
                    "z": 1.2,
                }
            },
        },
    )

    return fig
