import numpy as np

power_data = np.array([
    [120, 85, 95, 110],
    [200, 150, 180, 220],
    [50,  65,  40,  55]
])

filterz = power_data[power_data >= 100]

column_stats = power_data.mean(axis=0)

print("FILTERED HEAVY READINGS:", filterz)
print("DAILY AVERAGES:", column_stats)