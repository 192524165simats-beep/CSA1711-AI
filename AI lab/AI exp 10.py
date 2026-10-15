graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 4, 'B': 2, 'C': 1, 'D': 0}

open_list = [(h['A'], 0, 'A')]
visited = set()

while open_list:
    open_list.sort()
    f, g, node = open_list.pop(0)

    if node in visited:
        continue
    visited.add(node)

    if node == 'D':
        print("Goal reached:", node)
        print("Cost:", g)
        break

    for n, cost in graph[node]:
        if n not in visited:
            new_g = g + cost
            open_list.append((new_g + h[n], new_g, n))
