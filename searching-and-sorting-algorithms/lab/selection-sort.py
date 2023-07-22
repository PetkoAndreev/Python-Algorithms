nums = [int(x) for x in input().split()]

for index in range(len(nums)):
    curr_num = nums[index]
    min_num = curr_num
    min_index = index
    for next_index in range(index + 1, len(nums)):
        next_num = nums[next_index]
        if next_num < min_num:
            min_num = next_num
            min_index = next_index
    nums[index], nums[min_index] = nums[min_index], nums[index]

print(*nums, sep=' ')