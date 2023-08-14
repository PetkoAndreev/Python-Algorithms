from collections import deque


def best_sequence_of_matches(goals):
    n = len(goals)
    lis = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if goals[i] >= goals[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                prev[i] = j

    max_length = max(lis)
    end_index = lis.index(max_length)

    goals_list = deque([])

    while end_index >= 0:
        goals_list.appendleft(goals[end_index])
        end_index = prev[end_index]

    return goals_list


goals = [int(s) for s in input().split(', ')]
best_goals_sequence = best_sequence_of_matches(goals)
print(' '.join(str(goal) for goal in best_goals_sequence))
