using LinearAlgebra
using GLMakie

GLMakie.activate!()

fig = Figure(size=(1280, 720))

axis = Axis3(
    fig[1, 1],
    title="Rotated Anisotropic Quadratic"
)

# The surface itself

function f(x, y)
    return 3*(x^2) + 2*x*y + 2*(y^2)
end

xs = LinRange(-10, 10, 100)
ys = LinRange(-10, 10, 100)
zs = [f(x, y) for x in xs, y in ys]

surface!(axis, xs, ys, zs)

# Critical Point

crit_point = (0, 0, 0)
scatter!(axis, crit_point, markersize=30)

# The contour

contour3d!(axis, xs, ys, zs,
    levels=15,
    linewidth=2,
    color=:white
)

# The gradient descent

function gradient_x(x, y)
    return 6*x + 2*y
end

function gradient_y(x, y)
    return 2*x + 4*y
end

function descent_step(point, learning_rate)
    return point - learning_rate*[gradient_x(point[1], point[2]), gradient_y(point[1], point[2])]
end

learning_rate = 0.1
global previous_point = [10, 10]
global current_point = descent_step(previous_point, learning_rate)

trajectory = [Point2f(previous_point...), Point2f(current_point...)]

while norm(previous_point - current_point) > 0.05
    global previous_point = current_point
    global current_point = descent_step(current_point, learning_rate)
    push!(trajectory, Point2f(current_point...))
end

trajectory_3d = [Point3f(pt[1], pt[2], f(pt[1], pt[2]) + 10) for pt in trajectory]
scatter!(axis, trajectory_3d, markersize=30)
lines!(axis, trajectory_3d, color=:yellow)

# The vector field

axis2 = Axis(
    fig[1, 2],
    title="Vector Field",
    aspect=DataAspect()
)

xs_2d = LinRange(-100, 100, 10)
ys_2d = LinRange(-100, 100, 10)

us = [gradient_x(x, y) for x in xs_2d, y in ys_2d]
vs = [gradient_y(x, y) for x in xs_2d, y in ys_2d]
magnitudes = sqrt.(us .^ 2 + vs .^ 2)

arrows2d!(axis2, xs_2d, ys_2d, us, vs, color=magnitudes, colormap=:plasma, lengthscale=0.04)

# The critical point

crit_point_2d = (0, 0)
scatter!(axis2, crit_point_2d, markersize=30)

# Displaying

# save("f1.png", fig)

display(fig)
