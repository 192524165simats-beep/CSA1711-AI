import math

inputs = [1, 0]
weights = [0.5, 0.4]
bias = 0.1

total = sum(i * w for i, w in zip(inputs, weights)) + bias
output = 1 / (1 + math.exp(-total))

print("Network Output:", round(output, 3))
