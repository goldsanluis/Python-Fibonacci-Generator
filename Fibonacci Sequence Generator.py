def fibonacci(n):
    if n == 0:
        return[]
    sequence = [0, 1]
    for i in range(2, n):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    return sequence[:n]

print(fibonacci(2))
print(fibonacci(5))
print(fibonacci(21))