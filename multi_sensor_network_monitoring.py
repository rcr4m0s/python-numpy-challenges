import numpy as np

# Shape: (4, 3, 5) -> (Towers, Bands, Hours)
snr_data = np.array([
    # Tower 0
    [[-1.0, 12.5, 15.0, 18.2, -9.0],
     [22.0, 25.0, -5.0, 28.5, 30.0],
     [10.0, 11.5, 12.0, 14.0, 15.0]],

    # Tower 1
    [[ 8.0,  9.5, 11.0, -1.0, 14.0],
     [31.0, -2.0, 35.0, 38.0, 40.0],
     [18.0, 19.5, 21.0, 22.0, 24.0]],

    # Tower 2
    [[-4.0, 16.0, 17.5, 19.0, 20.0],
     [27.0, 29.0, 31.5, -8.0, 34.0],
     [ 5.0,  6.0,  7.5,  8.0,  9.0]],

    # Tower 3
    [[13.0, 14.5, -3.0, 17.0, 18.5],
     [41.0, 43.0, 45.0, 47.5, -6.0],
     [20.0, 22.0, 23.5, 25.0, 26.5]]
])


snr_data[snr_data < 0] = 0

crit_weak_sig = snr_data[(snr_data > 0.0) & (snr_data < 10.0)]
overall_ave = snr_data.mean(axis=(1,2))
peak_max = snr_data.max(axis=(0, 2))


print("CLEANED ARRAY")
print(snr_data)
print("CRITICAL SIGNAL LIST")
print(crit_weak_sig)
print("TOWER AVERAGE SNRs")
print(overall_ave)
print("BAND PEAK SNRs")
print(peak_max)
