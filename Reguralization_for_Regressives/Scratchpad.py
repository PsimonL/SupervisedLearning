import numpy as np


# https://www.geeksforgeeks.org/numpy-arrange-in-python/
# https://numpy.org/doc/stable/reference/generated/numpy.arange.html
power = 40
modulo = 10000
x1 = [(n ** power) % modulo for n in range(8)]
x2 = [(n ** power) % modulo for n in np.arange(8)]
print(x1)
print(x2)
print(np.arange(start=0, stop=10.1, step=0.1))