import numpy as np
import matplotlib.pyplot as plt

def char_lagrange(z, x):
    # Determine the length of the inputs
    n = len(x)
    m = len(z)
    
    # Initialize the matrix to store the evaluated Lagrange characteristic polynomials
    evaluated_characteristic_polynomial = [[0 for _ in range(m)] for _ in range(n)]
    
    # Evaluate the Lagrange characteristic polynomial at x_k with z_i
    for k in range(n):
        for i in range(m):
            result = 1
            for t in range(n):
                if t != k:
                    result = result * (z[i] - x[t]) / (x[k] - x[t])
            evaluated_characteristic_polynomial[k][i] = result
    return evaluated_characteristic_polynomial

def lagrange(z, x, y):
    # Obtain the evaluated Lagrange chracteristic polynomial at points z = [z_0,...,z_m]
    evaluated_characteristic_polynomial = char_lagrange(z, x)
    
    # Determine the length of y = [y_0,..., y_n]
    y_length = len(y)
    
    # Determine the length of z = [z_0,..., z_m]
    m = len(z)
    
    # Initialize the vector that will store the evaluated Lagrange interpolation formula
    evaluated_lagrange_interpolation_formula = [0 for _ in range(m)]
    
    # Evaluate the Lagrange interpolation formula at z
    for i in range(m):
        result = 0
        for k in range(y_length):
            result = result + (y[k] * evaluated_characteristic_polynomial[k][i])
        evaluated_lagrange_interpolation_formula[i] = result
    
    return evaluated_lagrange_interpolation_formula


# Given function to interpolate
def given_function(x):
    return 1 / (x**4 - 3*x**2 + 4)


"""
Plot the original function and Lagrange Interpolation for each set of nodes
"""


"""
Create the first figure for P4 with the original function
"""
# Nodes = 5
x_lagrange_0 = np.linspace(0, 3, num=5)
y_lagrange_0 = given_function(x_lagrange_0)
z_0 = np.linspace(0, 3, num=100)

plt.figure(figsize=(8, 6))
plt.plot(np.linspace(0, 3, 1000), given_function(np.linspace(0, 3, 1000)), label='f(x)', color='purple')
plt.plot(z_0, lagrange(z_0, x_lagrange_0, y_lagrange_0), label=r"P$_{4}$x", linestyle='--', color='#e54988')
plt.scatter(x_lagrange_0, y_lagrange_0, color='green', alpha=1, label='Nodes')  
plt.legend(loc="upper right")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Lagrange Interpolation P$_{4}$x with 5 equidistant nodes on [0, 3]")
plt.show()


"""
Create the second figure for P8 with the original function
"""
# Nodes = 9
x_lagrange_1 = np.linspace(0, 3, num=9)
y_lagrange_1 = given_function(x_lagrange_1)
z_1 = np.linspace(0, 3, num=100)

plt.figure(figsize=(8, 6))
plt.plot(np.linspace(0, 3, 1000), given_function(np.linspace(0, 3, 1000)), label='f(x)', color='purple')
plt.plot(z_1, lagrange(z_1, x_lagrange_1, y_lagrange_1), label=r"P$_{8}$x", linestyle='--', color='#fec97b')  
plt.scatter(x_lagrange_1, y_lagrange_1, color='green', alpha=1, label='Nodes')  
plt.legend(loc="upper right")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Lagrange Interpolation P$_{8}$x with 9 equidistant nodes on [0, 3]")
plt.show()


"""
Create the first figure for P13 with the original function
"""
# Nodes = 14
x_lagrange_2 = np.linspace(0, 3, num=14)
y_lagrange_2 = given_function(x_lagrange_2)
z_2 = np.linspace(0, 3, num=100)

plt.figure(figsize=(8, 6))
plt.plot(np.linspace(0, 3, 1000), given_function(np.linspace(0, 3, 1000)), label='f(x)', color='purple')
plt.plot(z_2, lagrange(z_2, x_lagrange_2, y_lagrange_2), label=r"P$_{13}$x", linestyle='--', color='#67bfaf')  
plt.scatter(x_lagrange_2, y_lagrange_2, color='green', alpha=1, label='Nodes')  
plt.legend(loc="upper right")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Lagrange Interpolation P$_{13}$x with 14 equidistant nodes on [0, 3]")
plt.show()


"""
Create the combined plot with all three Lagrange functions and the original function
"""
plt.figure(figsize=(8, 6))
plt.plot(np.linspace(0, 3, 1000), given_function(np.linspace(0, 3, 1000)), label='f(x)', color='purple')

# Plot all Lagrange functions
plt.plot(z_0, lagrange(z_0, x_lagrange_0, y_lagrange_0), label=r"P$_{4}$x", linestyle='--', color='#e54988')
plt.plot(z_1, lagrange(z_1, x_lagrange_1, y_lagrange_1), label=r"P$_{8}$x", linestyle='--', color='#fec97b')  
plt.plot(z_2, lagrange(z_2, x_lagrange_2, y_lagrange_2), label=r"P$_{13}$x", linestyle='--', color='#67bfaf')  

# Scatter plot for nodes (in green)
plt.scatter(x_lagrange_0, y_lagrange_0, color='green', alpha=1)  
plt.scatter(x_lagrange_1, y_lagrange_1, color='green', alpha=1)  
plt.scatter(x_lagrange_2, y_lagrange_2, color='green', alpha=1)  

# Add a dummy plot for the 'nodes' label
plt.scatter([], [], color='green', label='Nodes')

# Show combined plot
plt.legend(loc="upper right")
plt.xlabel("x")
plt.ylabel("y")
plt.title("All the Lagrange Interpolation with Original Function and Nodes")
plt.show()