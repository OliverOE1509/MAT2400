import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Examples on [0, 1]
# 1) Uniform convergence:   f_n(x) = x/(n+1)  -> f(x) = 0 uniformly
# 2) Pointwise (not uniform): g_n(x) = x^n    -> g(x) = 0 for x in [0,1), and g(1)=1
# ----------------------------

def f_n_uniform(x, n):
    return x / (n + 1)

def f_uniform_limit(x):
    return np.zeros_like(x)

def g_n_pointwise(x, n):
    return x**n

def g_pointwise_limit(x):
    # Limit of x^n on [0,1]: 0 for x<1, 1 for x=1
    y = np.zeros_like(x)
    y[np.isclose(x, 1.0)] = 1.0
    return y

def sup_error_uniform(xgrid, n):
    # Approximate sup-norm error for the uniform example on xgrid
    return np.max(np.abs(f_n_uniform(xgrid, n) - f_uniform_limit(xgrid)))

def sup_error_pointwise(xgrid, n):
    # Approximate sup-norm error for the pointwise-only example on xgrid
    return np.max(np.abs(g_n_pointwise(xgrid, n) - g_pointwise_limit(xgrid)))

def main():
    x = np.linspace(0, 1, 2000)

    ns = [1, 2, 5, 10, 25, 50, 100]

    fig = plt.figure(figsize=(12, 7))

    ax1 = plt.subplot2grid((2, 2), (0, 0))
    ax2 = plt.subplot2grid((2, 2), (0, 1))
    ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)

    # ----- Plot 1: Uniform convergence -----
    ax1.plot(x, f_uniform_limit(x), linewidth=3, label="limit f(x)=0")
    for n in ns:
        ax1.plot(x, f_n_uniform(x, n), label=f"n={n}")
    ax1.set_title("Uniform convergence: f_n(x)=x/(n+1) → 0")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_ylim(-0.05, 1.05)
    ax1.legend(fontsize=8)

    # ----- Plot 2: Pointwise but not uniform -----
    ax2.plot(x, g_pointwise_limit(x), linewidth=3, label="limit g(x)")
    for n in ns:
        ax2.plot(x, g_n_pointwise(x, n), label=f"n={n}")
    ax2.set_title("Pointwise (not uniform): g_n(x)=x^n on [0,1]")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_ylim(-0.05, 1.05)
    ax2.legend(fontsize=8)

    # ----- Plot 3: Sup error vs n (illustrates uniform vs not uniform) -----
    n_vals = np.arange(1, 201)
    sup_u = np.array([sup_error_uniform(x, n) for n in n_vals])
    sup_p = np.array([sup_error_pointwise(x, n) for n in n_vals])

    ax3.plot(n_vals, sup_u, label=r"$\|f_n-f\|_\infty$ for $f_n(x)=x/(n+1)$")
    ax3.plot(n_vals, sup_p, label=r"$\|g_n-g\|_\infty$ for $g_n(x)=x^n$")
    ax3.set_title("Approx sup-norm error: uniform goes to 0, pointwise-only stays ~1")
    ax3.set_xlabel("n")
    ax3.set_ylabel("approx sup error on grid")
    ax3.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
