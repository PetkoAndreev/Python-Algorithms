def cal_fib(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    result = cal_fib(n - 1, memo) + cal_fib(n - 2, memo)
    memo[n] = result
    return result


n = int(input())
print(cal_fib(n, {}))
