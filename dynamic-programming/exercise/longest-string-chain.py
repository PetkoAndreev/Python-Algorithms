from collections import deque

words = input().split()

size = [0] * len(words)
prev = [None] * len(words)

best_size = 0
best_index = 0

for index in range(len(words)):
    current_word = words[index]
    current_size = 1
    parent = None
    for prev_index in range(index - 1, -1, -1):
        prev_word = words[prev_index]

        if len(prev_word) >= len(current_word):
            continue

        if size[prev_index] + 1 >= current_size:
            current_size = size[prev_index] + 1
            parent = prev_index
    size[index] = current_size
    prev[index] = parent

    if current_size > best_size:
        best_size = current_size
        best_index = index

lis = deque()
index = best_index
while index is not None:
    lis.appendleft(words[index])
    index = prev[index]

print(*lis, sep=' ')