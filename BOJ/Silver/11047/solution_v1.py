import sys

input = sys.stdin.readline

N, K = map(int, input().split())
values = [int(input()) for _ in range(N)]

least = 0
for i in range(len(values) - 1, -1, -1):
    least += K // values[i]
    K %= values[i]
print(least)
