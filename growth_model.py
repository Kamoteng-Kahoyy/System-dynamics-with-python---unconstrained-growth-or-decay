# growth_model.py

import numpy as np
import matplotlib.pyplot as plt

# Function to model exponential growth
def exponential_growth(N0, r, t):
    return N0 * np.exp(r * t)

# Set initial conditions
N0 = 1  # Initial quantity
r = 0.1  # Growth rate

# Generate time points
t = np.linspace(0, 10, 100)

# Model exponential growth
N = exponential_growth(N0, r, t)

# Plot the results
plt.plot(t, N, label='Exponential Growth')
plt.xlabel('Time')
plt.ylabel('Quantity')
plt.legend()
plt.show()
