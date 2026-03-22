import numpy as np
import matplotlib.pyplot as plt

def manh(x, y):
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        raise TypeError
    
    if len(x) != len(y):
        raise ValueError
    
    lengths = []
    for i in len(x):
        lengths.append(np.abs(x[i] - y[i]))

    