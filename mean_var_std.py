import numpy as np

def calculate(list):
  if len(list) != 9:
     raise ValueError("List must contain nine numbers.")
  array = np.array(list)
  int_array = array.reshape(3,3)
  array = int_array / 1.0
  calculations = {
    "mean": [ array.mean(axis=0).tolist(), array.mean(axis=1).tolist(), array.mean()],
    "variance": [array.var(axis=0).tolist(),array.var(axis=1).tolist(), array.var()],
    "standard deviation": [array.std(axis=0).tolist(),array.std(axis=1).tolist(), array.std()],
    "max": [int_array.max(axis=0).tolist(),int_array.max(axis=1).tolist(), int_array.max()],
    "min": [int_array.min(axis=0).tolist(),int_array.min(axis=1).tolist(), int_array.min()],
    "sum": [int_array.sum(axis=0).tolist(),int_array.sum(axis=1).tolist(), int_array.sum()]
  }

  return calculations