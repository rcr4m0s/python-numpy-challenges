import numpy as np

power_kwh = np.array([12.5, 8.0, 25.4, 30.1, 15.0, 5.2, 28.0, 40.5, 18.2])

total_cost = power_kwh * 11
high_usage = power_kwh[power_kwh >= 20]

average_cost = total_cost.mean()
print("Average Cost:", average_cost)
sum_of_high_usage = high_usage.sum()
print("Sum of High Usage:", sum_of_high_usage)