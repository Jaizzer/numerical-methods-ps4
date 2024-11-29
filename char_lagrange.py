def char_lagrange(z, x):
    # Determine the length of the inputs
    x_length = len(x)
    z_length = len(z)
    
    # Initialize matrix to store the evaluated values
    matrix = [[0 for _ in range(z_length)] for _ in range(x_length)]

    return matrix


# Initialize interpolation values
x = [1, 2, 3, 4, 5]

# Initialize non-interpolation values
z = [1.5, 2.5, 3.5, 4.5, 5.5]
