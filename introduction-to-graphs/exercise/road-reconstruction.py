def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


buildings = int(input())
streets = int(input())

graph = []
[graph.append([]) for _ in range(buildings)]
edges = []
for _ in range(streets):
    first, second = [int(x) for x in input().split(' - ')]
    graph[first].append(second)
    graph[second].append(first)
    edges.append((min(first, second), max(first, second)))

print('Important streets:')

for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * buildings
    dfs(0, graph, visited)

    if not all(visited):
        print(first, second)

    graph[first].append(second)
    graph[second].append(first)
