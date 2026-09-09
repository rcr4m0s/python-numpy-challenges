import numpy as np

weights = np.array([498.5, 502.1, 495.0, 510.8, 488.2, 501.0, 505.4, 492.0, 500.0, 515.2])

weights_kg = weights / 1000

overweight_items = weights[weights >= 505.0]

average_weight_kg = weights_kg.mean()
print("Average Weight in KG:", average_weight_kg)
sum_of_overweight = overweight_items.sum()
print("Sum of Overweight Items:", sum_of_overweight)
