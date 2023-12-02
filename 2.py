from numpy.random import normal
import numpy as np
from matplotlib import pyplot as plt

arr = []
for _ in range(1200000):
    arr.append(normal(0))

arr = np.array(arr)

plt.hist(arr, bins=1000)
plt.show()
