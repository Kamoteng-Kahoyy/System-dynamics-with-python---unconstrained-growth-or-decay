import numpy as np
import matplotlib.pyplot as plt

sim_length = 48
growth_rate = 0.1
delta_t = 0.01
num_iter = int(sim_length/delta_t)
population = np.zeros(num_iter)
population[0] = 100

for i in range(num_iter-1):
    growth = growth_rate * population[i]
    population[i+1] = population[i] + growth * delta_t

    x_axis = np.arange(0, sim_length, delta_t)

    plt.plot(x_axis, population)
    plt.xlabel('Time (Hour)')
    plt.ylabel('Population')
    plt.title('Malthusian Growth Model for Bacteria Population Growth')
    plt.show()