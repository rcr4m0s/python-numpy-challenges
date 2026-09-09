import numpy as np

sensor_readings = np.array([
    [85.0, 102.5,  -99.0, 91.0],
    [78.5,  82.0,   88.5, 79.0],
    [115.0, 120.0, 108.5, -99.0],
    [65.0,  70.0,   72.5, 68.0],
    [-99.0, 95.0,  101.0, 98.5]
])

sensor_readings[sensor_readings < 0] = 0

filter = sensor_readings[sensor_readings < 90]
average = sensor_readings.mean(axis=0)

print("CLEAN PLANT SENSOR:", sensor_readings)
print("FILTERED TEMP:", filter)
print("AVERAGE:", average)
