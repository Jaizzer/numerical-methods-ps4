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


# Initialize the plot
plt.figure(num=1, dpi=120)

# Plot the original function
x_original = np.linspace(0, 3, num=1000)
y_original = given_function(x_original)
plt.plot(x_original, y_original, label='f(x)')
plt.legend(loc="upper right")

# Plot the lagrange interpolation function (nodes = 5)
x_lagrange_0 = np.linspace(0, 3, num=5)
y_lagrange_0 = given_function(x_lagrange_0)
z_0 = np.linspace(0, 3,num=100)
plt.plot(z_0, lagrange(z_0, x_lagrange_0, y_lagrange_0), label=r"P$_{4}$x")

# Plot the lagrange interpolation function (nodes = 9)
x_lagrange_1 = np.linspace(0, 3, num=9)
y_lagrange_1 = given_function(x_lagrange_1)
z_1 = np.linspace(0, 3,num=100)
plt.plot(z_1, lagrange(z_1, x_lagrange_1, y_lagrange_1), label=r"P$_{8}$x")

# Plot the lagrange interpolation function (nodes = 14)
x_lagrange_2 = np.linspace(0, 3, num=14)
y_lagrange_2 = given_function(x_lagrange_2)
z_2 = np.linspace(0, 3,num=100)
plt.plot(z_2, lagrange(z_2, x_lagrange_2, y_lagrange_2), label=r"P$_{13}$x")

plt.show()