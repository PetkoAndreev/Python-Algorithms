from collections import deque
from queue import PriorityQueue


def build_graph(roads):
    graph = {}
    for road in roads:
        city1, city2, distance = road.split(' - ')
        distance = int(distance)
        if city1 not in graph:
            graph[city1] = []
        if city2 not in graph:
            graph[city2] = []
        graph[city1].append((city2, distance))
        graph[city2].append((city1, distance))
    return graph


def find_critical_neighboors(graph, start, end, closed_roads):
    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        curr_distance, curr_city = pq.get()

        if curr_distance > distances[curr_city]:
            continue

        for neighbor, distance in graph[curr_city]:
            if (curr_city, neighbor) in closed_roads or (neighbor, curr_city) in closed_roads:
                continue

            total_distance = curr_distance + distance
            if total_distance < distances[neighbor]:
                distances[neighbor] = total_distance
                pq.put((total_distance, neighbor))

    path = deque([])
    current_city = end
    while current_city != start:
        path.appendleft(current_city)
        for neighbor, distance in graph[current_city]:
            if distances[current_city] == distances[neighbor] + distance:
                current_city = neighbor
                break

    path.appendleft(start)

    return path, distances[end]


num_roads = int(input())
roads = [input() for _ in range(num_roads)]
closed_roads_str = input()
closed_roads_list = [tuple(road.split('-')) for road in closed_roads_str.split(',')]
start_city = input()
end_city = input()

graph = build_graph(roads)
path, total_distance = find_critical_neighboors(graph, start_city, end_city, closed_roads_list)

print(' - '.join(path))
print(total_distance)
