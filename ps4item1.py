def char_lagrange(z, x):
    # Determine the length of the inputs
    x_length = len(x)
    z_length = len(z)
    
    # Initialize the matrix to store the evaluated Lagrange characteristic polynomials
    evaluated_characteristic_polynomial = [[0 for _ in range(z_length)] for _ in range(x_length)]
    
    # Evaluate the Lagrange characteristic polynomial at x_k with z_i
    for k in range(x_length):
        for i in range(z_length):
            result = 1
            for m in range(x_length):
                if m != k:
                    result = result * (z[i] - x[m]) / (x[k] - x[m])
            evaluated_characteristic_polynomial[k][i] = result
    return evaluated_characteristic_polynomial

def lagrange(z, x, y):
    # Obtain the evaluated Lagrange chracteristic polynomial at points z = [z_0,...,z_m]
    evaluated_characteristic_polynomial = char_lagrange(z, x)
    
    # Determine the length of y = [y_0,..., y_n]
    y_length = len(y)
    
    # Determine the length of z = [z_0,..., z_m]
    z_length = len(z)
    
    # Initialize the vector that will store the evaluated Lagrange interpolation formula
    evaluated_lagrange_interpolation_formula = [0 for _ in range(z_length)]
    
    # Evaluate the Lagrange interpolation formula at z
    for i in range(z_length):
        result = 0
        for k in range(y_length):
            result = result + (y[k] * evaluated_characteristic_polynomial[k][i])
        evaluated_lagrange_interpolation_formula[i] = result
    
    return evaluated_lagrange_interpolation_formula


# Given function to interpolate
def given_function(x):
    return 1 / (x**4 - 3*x**2 + 4)


def get_equidistant_nodes(left_endpoint, right_endpoint, number_of_nodes):
    # Determine the interval size
    interval_size = right_endpoint - left_endpoint
    
    # Determine the step size
    step_size = interval_size / (number_of_nodes - 1)
    
    # Initialize the array that will store all the equidistant nodes
    equidistant_nodes = [0 for _ in range(number_of_nodes)]
    for i in range(number_of_nodes):
        if i == 0:
            equidistant_nodes[i] = left_endpoint
        else:
            equidistant_nodes[i] = equidistant_nodes[i - 1] + step_size
    
    return equidistant_nodes

def get_y_values(x_values, function):
    # Determine the length of x_values
    x_length = len(x_values)
    
    # Initialize the array that will store the y-values
    y_values = [0 for _ in range(x_length)]
    
    # Evaluate the function using the given x_values
    for i in range(x_length):
        y_values[i] = function(x_values[i])
        
    return y_values