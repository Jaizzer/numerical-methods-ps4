import numpy as np
np.set_printoptions(legacy='1.25')

def NormalNCWeights(n):    
    # Initialize an arbitraty interval
    left_endpoint = -1
    right_endpoint = 1
    
    # Generate the equidistant nodes at the interval [left_endpoint, right_endpoint]
    x = np.linspace(left_endpoint, right_endpoint, num = n + 1)
        
    # Generate the Vandermonde matrix using the nodes
    V_transposed = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            V_transposed[i][j] = (x[j])**(i)
    
    # Initialize the matrix to store the evaluated integral of polynomial p_n(x) on [left_endpoint, right_endpoint]
    y = [0 for _ in range(n + 1)]
    
    # Evaluate the integral of polynomial p_n(x) on [left_endpoint, right_endpoint]
    for i in range(n + 1):
        y[i] = ((right_endpoint)**(i + 1) - (left_endpoint)**(i + 1)) /(i + 1) 
    
    # Calculate the normalization factor
    normalization_factor = n / (right_endpoint - left_endpoint)
    
    # Solve for the unnormalized weights
    unnormalized_weights = LU_solve(V_transposed, y)
    
    # Normalized the weights
    normalized_weights = unnormalized_weights * normalization_factor

    return normalized_weights


def LU_solve(A, r):
    # Note:
    # Ax = r where A = LU
    # <=> LUx = r where Ux = y
    # <=> Ly = r
    
    # Decompose A matrix into lower and upper triangular form: A = LU using SAXPY method
    L, U = perform_SAXPY_factorization(A)
        
    # Solve for y in Ly = r
    y = perform_forward_substitution(L, r)
    
    # Solve for x in Ux = y
    x = perform_backward_substitution(U, y)
    
    return x
    

def perform_backward_substitution(U, y): 
    # Determine the matrix size of the upper triangular matrix
    matrix_size = len(U)
    
    # Initialize the x-matrix
    x = np.array([0 for i in range(matrix_size)], dtype=np.float64)
    
    # Perform backward substitution
    for row in range(matrix_size):
        summation = 0
        for col in range(matrix_size - row, matrix_size):
            summation += U[matrix_size - (row + 1)][col] * x[col]
        x[matrix_size - (row + 1)] = (y[matrix_size - (row + 1)] - summation) / U[matrix_size - (row + 1)][matrix_size - (row + 1)]
    
    return x
    
    
def perform_forward_substitution(L, r):
    # Determine the matrix size of the lower triangular matrix
    matrix_size = len(L)
    
    # Initialize the y matrix
    y = np.array([0 for i in range(matrix_size)], dtype=np.float64)
    
    # Perform forward substitution
    for i in range(matrix_size):
        y[i] = r[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
    
    return y
            

def perform_SAXPY_factorization(array):
    # Determine the size of the array
    matrix_size = len(array)
    
    # Copy the matrix
    A = np.array(array, dtype=np.float64)
    
    # Store factorized lower and upper triangular inside A
    for k in range(matrix_size):
        for j in range(k + 1, matrix_size):
            A[j][k] = A[j][k] / A[k][k]
        for j in range(k + 1, matrix_size):          
            for i in range (k + 1, matrix_size):
                A[i][j] = A[i][j] - A[i][k] * A[k][j]
    
    # Extract lower and upper triangular from A
    return get_lower_and_upper_triangular_matrices(A)


def get_lower_and_upper_triangular_matrices(array):
    # Determine the size of the array
    matrix_size = len(array)
    
    # Copy the matrix
    A = np.array(array, dtype=np.float64)
    
    # Initialize lower and upper triangular matrices
    L = np.zeros((matrix_size, matrix_size), dtype=np.float64)
    U = np.zeros((matrix_size, matrix_size), dtype=np.float64)
    
    # Separate lower and upper triangular from A
    for i in range(matrix_size):
        L[i][i] = 1.0
        for j in range(i):
            L[i][j] = A[i][j]
        for j in range(i, matrix_size):
            U[i][j] = A[i][j]
        
    return [L, U]


def NCQuad(f, a, b, w):
    # Calculate the degree of precision by summing the normalized weights
    n = int(np.floor(np.sum(w)))
    
    # Calculate the step-size 'h'
    h = (b - a) / n
    
    # Obtain the actual weights from the normalized weights
    weights = w * h
    
    # Initialize the variable to store the Newton-Cotes-Quadrature
    newton_cotes_quadrature = 0
    
    # Calculate the the Newton-Cotes quadrature of f over the interval [a, b]
    for k in range(n):
        newton_cotes_quadrature += weights[k] * f(a + h*k)
        
    return newton_cotes_quadrature


def CompositeNCQuad(f, a, b, n, m):
    # Initialize the variable to store the Newton-Cotes-Quadrature
    newton_cotes_quadrature = 0
    
    # Calculate the number of subintervals
    for i in range(m):
        left_endpoint_of_current_subinterval = a + (b / m) * i 
        right_endpoint_of_current_subinterval = left_endpoint_of_current_subinterval + (b / m)
        newton_cotes_quadrature += NCQuad(f, left_endpoint_of_current_subinterval, right_endpoint_of_current_subinterval, NormalNCWeights(n))
        
    return newton_cotes_quadrature


# Given function to integrate
def given_function(x):
    return 1 / (x**4 - 3*x**2 + 4)

'''
Use CompositeNCQuad to approximate the given function at interval [0, 3] with [n, m] given by:
'''

# (i) [3,100], 
print(CompositeNCQuad(given_function, 0, 3, 3, 100))

# (ii) [4, 50], and 
print(CompositeNCQuad(given_function, 0, 3, 4, 50))

# (iii) [5,25]
print(CompositeNCQuad(given_function, 0, 3, 5, 35))