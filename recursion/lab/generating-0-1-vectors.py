def gen_vectors(index, vector):
    if index >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[index] = num
        gen_vectors(index + 1, vector)


n = int(input())
vector = [0] * n
gen_vectors(0, vector)
