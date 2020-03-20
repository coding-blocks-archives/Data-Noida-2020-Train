import os
import numpy as np

data = np.load("faces.npy")

X = data[:, 1:].astype(np.uint8)
y = data[:, 0]

print(X.shape, y.dtype)