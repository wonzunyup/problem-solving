import sys

input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    levels = [int(input()) for _ in range(n)]
    levels.sort()

    cut = int(n * 0.15 + 0.5)
    if cut > 0:
        levels = levels[cut:-cut]

    print(int(sum(levels) / len(levels) + 0.5))
