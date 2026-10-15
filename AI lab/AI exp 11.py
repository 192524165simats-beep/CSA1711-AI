colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

result = {}

for region in graph:
    for color in colors:
        if all(result.get(n) != color for n in graph[region]):
            result[region] = color
            break

print(result)
