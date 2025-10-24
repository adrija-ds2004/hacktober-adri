import math

data = [10, 20, 30, 40, 50]


n = len(data)

mean = sum(data) / n
variance = sum((x - mean) ** 2 for x in data) / n
std_dev = math.sqrt(variance)

print("Data:", data)
print("Mean (μ):", mean)
print("Variance (ϑ):", variance)
print("Standard Deviation (σ):", std_dev)
