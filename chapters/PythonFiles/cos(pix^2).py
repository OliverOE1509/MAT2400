import numpy as np
import matplotlib.pyplot as plt

cos = lambda x: np.cos(np.pi * x**2)

x = np.linspace(-10, 10, 1000)

plt.plot(x, cos(x))
plt.show()