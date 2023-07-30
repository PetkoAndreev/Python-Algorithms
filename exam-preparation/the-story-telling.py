from collections import deque


def dfs(node, graph, visited, cycles):
    if node in cycles:
        raise Exception('Cycle has been detected. Invalid topological sorting.')
    if node in visited:
        return
    visited.add(node)
    cycles.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, cycles)
    cycles.remove(node)
    sorted_nodes.appendleft(node)



line_input = input()
graph = {}

while line_input != 'End':
    line_parts = line_input.split('->')
    node = line_parts[0].strip()
    children = line_parts[1].strip().split() if line_parts[1] else []
    graph[node] = children
    line_input = input()

visited = set()
cycles = set()

sorted_nodes = deque()
for node in graph:
    dfs(node, graph, visited, cycles)

print(*sorted_nodes, sep=' ')