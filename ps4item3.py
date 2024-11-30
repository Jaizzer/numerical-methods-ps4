import numpy as np

def NormalNCWeights(n):
    # Initialize the matrix to store the 'n + 1' normalized weights
    normalized_weights = [0 for _ in range(n + 1)]
    
    # Generate the equidistant nodes at the interval [-1, 1]
    x = np.linspace(-1, 1, num = n + 1)
    
    # Generate the Vandermonde matrix using the nodes
    V = np.vander(x)
        
    # Initialize the matrix to store the evaluated integral of polynomial p_n(x) on [-1, 1]
    y = [0 for _ in range(n + 1)]
    
    return normalized_weights