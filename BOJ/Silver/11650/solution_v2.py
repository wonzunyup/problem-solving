import sys

input = sys.stdin.readline

N = int(input())
spots = [tuple(map(int, input().split())) for _ in range(N)]
spots.sort()

for x, y in spots:
    print(x, y)
