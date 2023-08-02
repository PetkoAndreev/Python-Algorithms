def find_combinations(num, combinations):
    if num == 0:
        print(" + ".join(str(num) for num in combinations))
        return

    if combinations:
        current_range = min(num, combinations[-1])
    else:
        current_range = num

    for i in range(current_range, 0, -1):
        find_combinations(num - i, combinations + [i])


num = int(input())
combinations = []
find_combinations(num, combinations)
