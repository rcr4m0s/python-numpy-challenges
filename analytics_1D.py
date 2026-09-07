import numpy as np

sales = np.array([1200, 4500, 800, 3200, 6000, 1500, 900, 7500, 2100, 4000, 1100, 5200])

net_sales = sales * 0.88
peak_sales = sales[sales >= 4000]

average_net_sales = net_sales.mean()
total_revenue = peak_sales.sum()

print("Net sales: ", net_sales)
print("Peak sales; ", peak_sales)
print("Average net sale:", average_net_sales)
print("Sum of peak sales:", total_revenue)

#a