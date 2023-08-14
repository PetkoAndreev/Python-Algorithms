def find_all_paths(row, col, maze, direction, path, all_paths):
    if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]):
        return
    if maze[row][col] == '#':
        return
    if maze[row][col] == 'V':
        return
    path.append(direction)
    if maze[row][col] == 'E':
        all_paths.append(path[:])  # Make a copy of the current path and add it to all_paths
    else:
        maze[row][col] = 'V'
        find_all_paths(row, col - 1, maze, 'L', path, all_paths)
        find_all_paths(row, col + 1, maze, 'R', path, all_paths)
        find_all_paths(row - 1, col, maze, 'U', path, all_paths)
        find_all_paths(row + 1, col, maze, 'D', path, all_paths)

        maze[row][col] = '.'
    path.pop()


size = int(input())
maze = []

for _ in range(size):
    maze.append(list(input()))

all_paths = []
find_all_paths(0, 0, maze, '', [], all_paths)

shortest_path = float('inf')
for path in all_paths:
    if (len(path) - 1) < shortest_path:
        shortest_path = len(path) - 1
print(shortest_path)
# 4
# S...
# .##E
# .##.
# ....