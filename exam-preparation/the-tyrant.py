def min_sum_seq(num_sequence):
    size = len(num_sequence)
    dp = [0] * size

    if size < 5:
        return min(num_sequence)

    dp[0:4] = num_sequence[0:4]

    for i in range(4, size):
        dp[i] = num_sequence[i] + min(dp[i - 4: i])

    return min(dp[size - 4:size])


num_sequence = [int(x) for x in input().split()]
print(min_sum_seq(num_sequence))
