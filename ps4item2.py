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

def lagrange2D(zx, zy, x, y, w):
    # Determine the length of x
    x_length = len(x)
    
    # Determine the length of y
    y_length = len(y)
    
    # Determine the length of zx
    zx_length = len(zx)
    
    # Determine the lenght of zy
    zy_length = len(zy)
    
    # Initialize the matrix to store the evaluated Lagrange characteristic polynomials on the x-axis
    evaluated_characteristic_polynomial_x = [[0 for _ in range(zx_length)] for _ in range(x_length)]
    
    # Initialize the matrix to store the evaluated Lagrange characteristic polynomials on the y-axis
    evaluated_characteristic_polynomial_y = [[0 for _ in range(zy_length)] for _ in range(y_length)]
    
    # Initialize the vector that will store the evaluated 2D Lagrange interpolation formula
    evaluated_lagrange_interpolation_formula_2D = [[0 for _ in range(zy_length)] for _ in range(zx_length)]    

    return 