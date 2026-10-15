
from collections import deque
import matplotlib.pyplot as plt

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

q = deque(['A'])
visited = []

while q:
    node = q.popleft()
    if node not in visited:
        visited.append(node)
        q.extend(graph[node])

print("BFS Traversal:", visited)

plt.figure(figsize=(8, 2))
plt.axis('off')
plt.text(0.5, 0.5, "BFS Traversal:\n" + str(visited),
         ha='center', va='center', fontsize=14)
plt.savefig("Outputs/bfs_output.png", bbox_inches='tight')
plt.close()
