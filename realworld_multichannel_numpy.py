import numpy as np

# Shape: (3, 4, 3) -> (Regions, Stores, Categories)
inventory = np.array([
    # Region 0 (Luzon)
    [[150, -5, 200],
     [80, 120, 45],
     [300, 250, -12],
     [90, 110, 85]],

    # Region 1 (Visayas)
    [[60, 40, -1],
     [220, 180, 190],
     [15, 30, 25],
     [130, 140, -8]],

    # Region 2 (Mindanao)
    [[100, 90, 110],
     [-15, 200, 150],
     [70, 85, 95],
     [180, 160, 175]]
])


inventory[inventory < 0] = 0

below_safety_threshold = inventory[(inventory < 50) & (inventory > 0 )]
total_inventory_region = inventory.sum(axis=(1, 2))
average_stock_product = inventory.mean(axis=(0, 1))

print("CLEANED INVENTORY:", inventory)
print("SAFETY STOCK ITEMS (< 50 & > 0):")
print(below_safety_threshold)
print("TOTAL PER REGION:", total_inventory_region)
print("CATEGORY AVERAGE:", average_stock_product)

