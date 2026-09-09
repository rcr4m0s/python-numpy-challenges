import numpy as np

# 1. Raw readings (1D array na may 10 values)
readings = np.array([25.4, 28.1, -5.0, 30.2, -1.2, 27.8, 29.0, 31.5, -9.9, 26.3])

# 2. Boolean Masking: Palitan ang lahat ng less than 0 ng 0
# Hint: Gamitin ang readings[readings < 0]
readings[readings < 0] = 0

# 3. Reshape: Gawing 2x5 matrix ang 1D array
# Hint: Gamitin ang .reshape(rows, cols)
matrix = readings.reshape(2, 5)

# 4. Axis Stats: Kunin ang mean bawat row (axis=1)
# Hint: np.mean(matrix, axis=1)
row_mean = np.mean(matrix, axis=1)

print("Cleaned Matrix:\n", matrix)
print("Row Mean:", row_mean)