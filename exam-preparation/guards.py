def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    start, end = [int(x) for x in input().split()]
    graph[start].append(end)

start_node = int(input())
visited = [False] * (nodes + 1)

dfs(start_node, graph, visited)
not_visited = []

for num in range(1, len(visited)):
    if num != 0 and not visited[num]:
        not_visited.append(num)

print(*sorted(not_visited), sep=' ')
