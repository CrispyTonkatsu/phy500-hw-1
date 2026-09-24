using GLMakie

GLMakie.activate!()

fig = Figure(size=(600, 400))

axis = Axis3(
    fig[1, 1],
    title="Rotated Anisotropic Quadratic"
)

xs = LinRange(-100, 100, 100)
ys = LinRange(-100, 100, 100)
zs = [3*(x^2) + 2*x*y + 2*(y^2) for x in xs, y in ys]

surface!(axis, xs, ys, zs)

contour3d!(axis, xs, ys, zs,
    levels=15,
    linewidth=2,
    color=:white
)

axis2 = Axis(
    fig[1, 2],
    title="Vector Field",
    aspect=DataAspect()
)

xs_2d = LinRange(-100, 100, 10)
ys_2d = LinRange(-100, 100, 10)

us = [6*x + 2*y for x in xs_2d, y in ys_2d]
vs = [2*x + 4*y for x in xs_2d, y in ys_2d]
magnitudes = sqrt.(us .^ 2 + vs .^ 2)

arrows2d!(axis2, xs_2d, ys_2d, us, vs, color=magnitudes, colormap=:plasma, lengthscale=0.04)

display(fig)
