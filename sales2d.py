import numpy as np
# Row 0: Store A | Row 1: Store B
# Cols: Q1, Q2, Q3
sales = np.array([
    [10000, 15000, 20000],
    [8000, 12000, 18000]
])

print(sales.shape)

net_sales = sales * 0.9

total_sales = sales.sum(axis=1)
print("Total sales:", total_sales)
average_sales = sales.mean(axis=0)
print("Average sales per Quarter:", average_sales) 