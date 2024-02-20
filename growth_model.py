import numpy 
import matplotlib.pyplot

sim_length = 48
growth_rate = 0.1
delta_t = 0.01
num_iter = int(sim_length / delta_t)
population = numpy.zeros(num_iter)
population[0] = 100

for i in range(num_iter - 1):
    growth = growth_rate * population[i]
    population[i + 1] = population[i] + growth * delta_t

x_axis = numpy.arange(0, sim_length, delta_t)

matplotlib.pyplot.plot(x_axis, population)
matplotlib.pyplot.xlabel('Time (Hour)')
matplotlib.pyplot.ylabel('Population')
matplotlib.pyplot.title('Malthusian Growth Model for Bacteria Population Growth')
matplotlib.pyplot.show()