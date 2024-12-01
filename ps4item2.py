def char_lagrange(z, x):
    # Determine the length of the inputs
    nx = len(x)
    z_length = len(z)
    
    # Initialize the matrix to store the evaluated Lagrange characteristic polynomials
    evaluated_characteristic_polynomial = [[0 for _ in range(z_length)] for _ in range(nx)]
    
    # Evaluate the Lagrange characteristic polynomial at x_k with z_i
    for k in range(nx):
        for i in range(z_length):
            result = 1
            for m in range(nx):
                if m != k:
                    result = result * (z[i] - x[m]) / (x[k] - x[m])
            evaluated_characteristic_polynomial[k][i] = result
    return evaluated_characteristic_polynomial

def lagrange2D(zx, zy, x, y, w):
    # Determine the length of x
    nx = len(x)
    
    # Determine the length of y
    ny = len(y)
    
    # Determine the length of zx
    mx = len(zx)
    
    # Determine the lenght of zy
    my = len(zy)
    
    # Evaluate the Lagrange characteristic polynomials on the x-axis
    evaluated_characteristic_polynomial_x = char_lagrange(zx, x)
    
    # Evaluate the Lagrange characteristic polynomials on the y-axis
    evaluated_characteristic_polynomial_y = char_lagrange(zy, y)

    # Initialize the vector that will store the evaluated 2D Lagrange interpolation formula
    evaluated_lagrange_interpolation_formula_2D = [[0 for _ in range(my)] for _ in range(mx)]    

    # Evaluate the 2D Lagrange interpolation formula
    for zx_index in range(mx):
        for zy_index in range(my):
            outer_result = 0
            for i in range(nx):
                inner_result = 0
                for j in range(ny):
                    inner_result += w[i][j] * evaluated_characteristic_polynomial_x[i][zx_index] * evaluated_characteristic_polynomial_y[j][zy_index]
                outer_result += inner_result
            evaluated_lagrange_interpolation_formula_2D[zx_index][zy_index] = outer_result
            
    return evaluated_lagrange_interpolation_formula_2D   