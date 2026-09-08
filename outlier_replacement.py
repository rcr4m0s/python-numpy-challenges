import numpy as np

response_times = np.array([120, 450, 210, 320, 180, 500, 250, 190])

response_times[response_times > 300] = 300

std = np.std(response_times)

print("CAPPED RESPONSE TIMES:", response_times)
print("STANDARD DEVIATION:", std)