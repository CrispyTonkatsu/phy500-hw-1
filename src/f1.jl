using LinearAlgebra
using GLMakie

using hw1

GLMakie.activate!()

fig = Figure(size=(720, 720))

axis = Axis3(
    fig[1, 1],
    title="Rotated Anisotropic Quadratic",
    azimuth=3*π/4
)

function f(x, y)
    return 3*(x^2) + 2*x*y + 2*(y^2)
end

function gradient_x(x, y)
    return 6*x + 2*y
end

function gradient_y(x, y)
    return 2*x + 4*y
end

hw1.render_surface!(axis, f)

crit_point = (0, 0, 0)
hw1.render_crit_points!(axis, crit_point, 50)

# The gradient descent

learning_rate = 0.1
start_point = [10, 10]
hw1.render_gradient_descent!(axis, start_point, 0.1, f, gradient_x, gradient_y)

# The vector field

fig2 = Figure(size=(720, 720))

axis2 = Axis(
    fig2[1, 1],
    title="Quadratic Vector Field",
    aspect=DataAspect()
)

hw1.render_vector_field!(axis2, gradient_x, gradient_y)

# The critical point

crit_point_2d = (0, 0)
hw1.render_crit_points!(axis2, [crit_point], 30)

# Saving to images
save("f1-graph.png", fig)
save("f1-vector-field.png", fig2)

# Displaying
display(fig)
display(GLMakie.Screen(), fig2)
