import numpy as np

defects = np.array([
    [5, 2, 8, 1],
    [0, 4, 3, 2],
    [9, 6, 7, 5]
])

line2_defects = defects[2, :]
print("Defect count of Line 2:", line2_defects)                  
day3_defects = defects[:, 2]
print("Defects of day 3 across all lines:", day3_defects)


total_defects_per_line = defects.sum(axis=1)
print("Total defects per line:", total_defects_per_line)
average_defects_per_day = defects.mean(axis=0)
print("Average defects per day:", average_defects_per_day)
