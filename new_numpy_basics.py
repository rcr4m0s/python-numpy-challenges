import numpy as np

scores = np.array([45, 88, 92, 60, 71, 35, 100, 52])

passed_mask = scores >= 75
print("Mask (True/False):", passed_mask)

passing_scores = scores[scores >= 75]
print("Passing scores only:", passing_scores)

failing_scores = scores[scores < 60]
print("Failing score:", failing_scores)

average_score = scores.mean()
print("Average score:", average_score)
highest_scores = scores.max()
print("Highest score:", highest_scores)

average_passing_scores = passing_scores.mean()
print("Average of passing score:", average_passing_scores)