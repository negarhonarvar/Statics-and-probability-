import math

import matplotlib.pyplot
import numpy


# Q2
# Geometric distribution Formula :  ((1 - probability)^(attempt - 1)) * probability
def geometric_distribution(attempt, probability):
    return math.pow((1 - probability), (attempt - 1)) * probability


# attempt = 1,2,3,4 : for this question
matplotlib.pyplot.rc('xtick')
matplotlib.pyplot.rc('ytick')
matplotlib.pyplot.xticks(range(1, 4))
y_ticks = []
for i in range(1, 4):
    y_ticks.append(geometric_distribution(i, 0.25))

matplotlib.pyplot.bar(list(numpy.arange(1, 3 + 1)), y_ticks)
matplotlib.pyplot.show()
print(y_ticks)
