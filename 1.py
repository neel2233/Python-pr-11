from scipy import signal
from matplotlib import pyplot as plt
import numpy as np

t = np.arange(0, 1, 0.001)
x = signal.square(2 * np.pi * 5 * t)

plt.plot(t, x)
plt.show()
