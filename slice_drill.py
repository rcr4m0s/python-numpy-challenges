import numpy as np

ping = np.array([
    [10, 25, 30],
    [45, 12, 18],
    [50, 60, 40]
])

pong = ping[:, 1]
print("Slice:", pong)
mean = ping.mean(axis=1)
print("Average response time:", mean)
