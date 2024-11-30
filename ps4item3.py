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
    unnormalized_weights = (np.linalg.solve(V_transposed, y)) 
    
    # Normalized the weights
    normalized_weights = unnormalized_weights * normalization_factor

    return normalized_weights