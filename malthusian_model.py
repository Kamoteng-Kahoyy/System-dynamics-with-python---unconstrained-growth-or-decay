import numpy as np
import matplotlib.pyplot as plt

# Get user inputs
sim_length = float(input("Enter simulation length in hours: "))
growth_rate = float(input("Enter growth rate: "))
delta_t = float(input("Enter time step (delta_t): "))

# Calculate the number of iterations
num_iter = int(sim_length / delta_t)

# Initialize the population array
population = np.zeros(num_iter)
population[0] = float(input("Enter initial population: "))

# Simulate population growth
for i in range(num_iter - 1):
    growth = growth_rate * population[i]
    population[i + 1] = population[i] + growth * delta_t

# Generate time points
x_axis = np.arange(0, sim_length, sim_length / num_iter)

# Plot the results
plt.plot(x_axis, population)
plt.xlabel('Time (Hour)')
plt.ylabel('Population')
plt.title('Malthusian Growth Model for Bacteria Population Growth')
plt.show()
