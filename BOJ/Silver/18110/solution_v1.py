import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
else:
    levels = [int(input()) for _ in range(n)]
    num = int(n * 0.15 + 0.5)

    levels.sort()
    if num > 0:
        levels = levels[num:-num]
    print(int(sum(levels) / len(levels) + 0.5))
