import numpy as np
raw_data = np.array([10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 40])

sensor_matrix = raw_data.reshape(3, 4)

slice_masking_combo = sensor_matrix[1]
wow = slice_masking_combo[slice_masking_combo > 20]
print("Filter:", wow)

new_row = np.array([[50, 55, 60, 65]])
combined_matrix = np.vstack((sensor_matrix, new_row))

print("Endable:", combined_matrix)