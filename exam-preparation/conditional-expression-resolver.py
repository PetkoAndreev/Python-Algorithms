ternary_expressions = input().split()
ternary_expression_index = []

for i in range(len(ternary_expressions)):
    if ternary_expressions[i] == '?':
        ternary_expression_index.append(i)

current_result = None
for idx in reversed(ternary_expression_index):
    expected = ternary_expressions[idx - 1]
    if_true = ternary_expressions[idx + 1]
    if_false = ternary_expressions[idx + 3]
    if expected == 't':
        current_result = if_true
    else:
        current_result = if_false
    ternary_expressions.insert(idx + 4, current_result)
    ternary_expressions = ternary_expressions[0:idx - 1] + ternary_expressions[idx + 4:]

print(current_result)
