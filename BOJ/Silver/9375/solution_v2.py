from collections import defaultdict
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    clothes = defaultdict(int)

    for _ in range(n):
        clothe, type = input().split()
        clothes[type] += 1

    result = 1
    for cnt in clothes.values():
        result *= cnt + 1

    sys.stdout.write(str(result - 1) + "\n")
