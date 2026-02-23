N = int(input())

generator = 0
start = max(0, N - 9 * len(str(N)))

for i in range(start, N):
    total = i
    for digit in str(i):
        total += int(digit)
    if total == N:
        generator = i
        break

print(generator)
