def char_lagrange(z, x):
    # Determine the length of the inputs
    x_length = len(x)
    z_length = len(z)
    
    # Initialize matrix to store the evaluated Lagrange characteristic polynomials
    matrix = [[0 for _ in range(z_length)] for _ in range(x_length)]
    
    # Evaluate the Lagrange characteristic polynomial at x_k with z_i
    for k in range(x_length):
        for i in range(z_length):
            result = 1
            for m in range(x_length):
                if m != k:
                    result = result * (z[i] - x[m]) / (x[k] - x[m])
            matrix[k][i] = result
    return matrix


# Initialize interpolation values
x = [1, 2, 3, 4, 5]

# Initialize non-interpolation values
z = [1.5, 2.5, 3.5, 4.5, 5.5]

# Initialize y-interpolation values
y = [12, 34, 56, 58, 90]

char_lagrange(z, x)


def lagrange(z, x, y):
    # Obtain the evaluated Lagrange chracteristic polynomial at points z = [z_0,...,z_m]
    evaluated_characteristic_polynomial = char_lagrange(z, x)
    
    # Determine the length of y = [y_0,..., y_n]
    y_length = len(y)
    
    # Determine the length of z = [z_0,..., z_m]
    z_length = len(z)
    
    # Initialize the vector that will store the evaluated Lagrange interpolation formula
    vector = [0 for _ in range(z_length)]
    
    return vector
