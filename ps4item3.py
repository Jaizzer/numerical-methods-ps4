import numpy as np

def NormalNCWeights(n):    
    # Generate the equidistant nodes at the interval [-1, 1]
    x = np.linspace(-1, 1, num = n + 1)
    
    # Generate the Vandermonde matrix using the nodes
    V = np.vander(x)
        
    # Initialize the matrix to store the evaluated integral of polynomial p_n(x) on [-1, 1]
    y = [0 for _ in range(n + 1)]
    
    # Evaluate the integral of polynomial p_n(x) on [-1, 1]
    for i in range(n + 1):
        y[i] = ((1)**(i + 1))/(i + 1) - ((-1)**(i + 1))/(i + 1)
        
    # Solve for the weights
    normalized_weights = np.linalg.solve(V, y)
            
    return normalized_weights