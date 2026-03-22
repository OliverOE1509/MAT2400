import numpy as np
import matplotlib.pyplot as plt

def H(x):
    return np.abs(np.sin(x) - np.cos(x))

def dH_numeric(x, step):
    return (H(x + step) - H(x)) / step

x = np.linspace(0, 1, 1000)

plt.plot(x, H(x), label="H(x)=|sin x - cos x|")
plt.plot(x, dH_numeric(x, 1e-5), label="numeric derivative")
plt.grid(True)
plt.legend()
plt.show()
