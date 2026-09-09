import numpy as np

orders = np.array([
    [45, -10, 80],
    [120, 150, -5],
    [30, 65, 50],
    [200, 180, 220]
])

orders[orders < 0 ] = 0

high_perfor = orders[orders >= 100]
branch_analy = orders.mean(axis=1)

print("CLEANED:", orders)
print("HIGH VOLUME ORDERS (>= 100):", high_perfor)
print("BRANCH AVERAGES:", branch_analy)