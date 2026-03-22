import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos( np.pi * x**2)

def sup_dist_shift(r):
    # For f(x)=2x+1: |f(x+r)-f(x)| = 2|r| for all x
    return 2 * abs(r)

xs = np.linspace(-10, 10, 800)
shifts = list(range(10, 0, -5))

fig, ax = plt.subplots(figsize=(8, 4))

#for r in shifts:
    #ax.plot(xs, f(xs + r), label=f"r={r}, sup= {sup_dist_shift(r)}")

ax.plot(xs, f(xs), linewidth=3, label="r=0 (original)")
ax.set_xlabel("x")
ax.set_ylabel("f(x+r)")
ax.grid(True)
ax.legend(ncol=2, fontsize=8)
plt.tight_layout()
plt.show()
