import numpy as np

data = np.array([10, 25, 40, 55, 70, 85, 100])

min_val = np.min(data)
max_val = np.max(data)

norm_data = (data - min_val) / (max_val - min_val)
high_values = norm_data[norm_data > 0.5]

print("NORM DATA:", norm_data)
print("HIGH VALUES:", high_values)