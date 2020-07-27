import numpy as np

def sigmoid(X):
  return 1 / (1 + np.exp(-x))

X = np.array([1, 2])
W = np.array([[1, 3, 5], [2, 4, 6]])
Y = np.dot(X, W)
print(Y)