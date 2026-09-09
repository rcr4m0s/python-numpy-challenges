import numpy as np

batch_a = np.array([
    [1, 2],
    [3, 4]
])

batch_b = np.array([
    [5, 6],
    [7, 8]
])
combined = np.vstack((batch_a, batch_b))
print(combined)
print(batch_b.shape)
print(batch_a.shape)
