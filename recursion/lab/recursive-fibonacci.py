# def calc_fib(number):
#     if number <= 1:
#         return 1
#     return calc_fib(number - 1) + calc_fib(number - 2)
# n = int(input())
# print(calc_fib(n))
# print(calc_fib(10))  # 89
# print(calc_fib(50))

# Iterative solution is much faster
def iterative_fib(number):
    fib0 = 1
    fib1 = 1
    result = 0
    for _ in range(number - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result

n = int(input())
print(iterative_fib(n))
