import numpy as np

# Shape: (2, 3, 4) -> (Factory Lines, Machines, Intervals)
factory_data = np.array([
    # Factory Line 0
    [[88.0, -99.0, 92.0, 95.0],
     [75.0,  80.0, 85.0, 78.0],
     [105.0, 110.0, -99.0, 115.0]],
    
    # Factory Line 1
    [[60.0,  65.0, 70.0,  68.0],
     [-99.0, 90.0, 95.0,  92.0],
     [120.0, 125.0, 130.0, 128.0]]
])

factory_data[factory_data < 0 ] = 0

min_val = np.min(factory_data)
max_val = np.max(factory_data)

norm_formu = (factory_data - min_val) / (max_val - min_val)

average = factory_data.mean(axis=(1, 2))

print("CLEARED 3D ARRAY:", factory_data)
print("NORMALIZED ARRAY:", norm_formu)
print("AVERAGE:", average)
