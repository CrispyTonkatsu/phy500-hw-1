module hw1

using LinearAlgebra
using GLMakie

function render_surface!(axis, f)
    xs = LinRange(-10, 10, 100)
    ys = LinRange(-10, 10, 100)
    zs = [f(x, y) for x in xs, y in ys]

    surface!(axis, xs, ys, zs)

    contour3d!(axis, xs, ys, zs,
        levels=15,
        linewidth=2,
        color=:white
    )
end

function render_crit_points!(axis, points, points_size)
    scatter!(axis, points, markersize=points_size)
end

function descent_step(point, learning_rate, gradient_x, gradient_y)
    return point - learning_rate*[gradient_x(point[1], point[2]), gradient_y(point[1], point[2])]
end

function render_gradient_descent!(axis, starting_point, learning_rate, f, gradient_x, gradient_y)
    global previous_point = starting_point
    global current_point = descent_step(previous_point, learning_rate, gradient_x, gradient_y)

    trajectory = [Point2f(previous_point...), Point2f(current_point...)]

    while norm(previous_point - current_point) > 0.05
        global previous_point = current_point
        global current_point = descent_step(current_point, learning_rate, gradient_x, gradient_y)
        push!(trajectory, Point2f(current_point...))
    end

    trajectory_3d = [Point3f(pt[1], pt[2], f(pt[1], pt[2]) + 10) for pt in trajectory]
    scatter!(axis, trajectory_3d, markersize=30)
    lines!(axis, trajectory_3d, color=:yellow)
end

function render_vector_field!(axis, gradient_x, gradient_y)
    xs = LinRange(-100, 100, 10)
    ys = LinRange(-100, 100, 10)

    us = [gradient_x(x, y) for x in xs, y in ys]
    vs = [gradient_y(x, y) for x in xs, y in ys]
    magnitudes = sqrt.(us .^ 2 + vs .^ 2)

    arrows2d!(axis, xs, ys, us, vs, color=magnitudes, colormap=:plasma, lengthscale=0.04)
end

end
