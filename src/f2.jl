using LinearAlgebra
using GLMakie

using hw1

GLMakie.activate!()

fig = Figure(size=(720, 720))

axis = Axis3(
    fig[1, 1],
    title="Double Well",
)

function f(x, y)
    return (x^2 - 1)^2 + y^2
end

function gradient_x(x, y)
    return 4*x^3 - 4x
end

function gradient_y(x, y)
    return 2*y
end

hw1.render_surface!(axis, f)

# crit_points = [(-1, 0, f(-1, 0)), (0, 0, f(0, 0)), (1, 0, f(1, 0))]
# hw1.render_crit_points!(axis, crit_points, 50)

# The gradient descent

# learning_rate = 0.1
# start_point = [10, 10]
# hw1.render_gradient_descent!(axis, start_point, 0.1, f, gradient_x, gradient_y)

# The vector field

fig2 = Figure(size=(720, 720))

axis2 = Axis(
    fig2[1, 1],
    title="Double Well Vector Field",
    aspect=DataAspect()
)

hw1.render_vector_field!(axis2, gradient_x, gradient_y)

# The critical point

crit_points_2d = [(-1, 0), (0, 0), (1, 0)]
hw1.render_crit_points!(axis2, crit_points_2d, 30)

# Saving to images
save("f2-graph.png", fig)
save("f2-vector-field.png", fig2)

# Displaying
display(fig)
# display(GLMakie.Screen(), fig2)
