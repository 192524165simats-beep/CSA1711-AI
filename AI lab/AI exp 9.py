from itertools import permutations

cost = [[0, 10, 15],
        [10, 0, 20],
        [15, 20, 0]]

cities = [1, 2]
min_cost = float('inf')

for p in permutations(cities):
    path = (0,) + p + (0,)
    total = sum(cost[path[i]][path[i+1]]
                for i in range(len(path)-1))

    if total < min_cost:
        min_cost = total
        best_path = path

print("Path:", best_path)
print("Minimum Cost:", min_cost)
