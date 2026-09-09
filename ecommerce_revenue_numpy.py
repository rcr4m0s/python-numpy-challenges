import numpy as np

sales_data = np.array([
    [150.5, 200.0, -15.0, 180.2],
    [80.0,   95.5, 110.0,  70.0],
    [310.0, 280.5, 290.0, 350.0],
    [-5.0,  120.0, 140.0, 160.0],
    [50.0,   45.0,  60.0,  40.0]
])

sales_data[sales_data < 0] = 0.0

filter = sales_data[sales_data > 150.0]
total = sales_data.sum(axis=1)
average = sales_data.mean(axis=0)

print("CLEARED MATRIX:", sales_data)
print("HIGH PERFORMING SALES LIST:", filter)
print("TOTAL REVENUES:", total)
print("QUARTERLY AVERAGE:", average)
