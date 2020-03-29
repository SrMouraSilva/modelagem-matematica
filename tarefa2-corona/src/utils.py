import numpy as np


def rmse(data, reconstructed):
    return np.sqrt(np.mean(np.square(data - reconstructed)))