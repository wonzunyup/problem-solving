import sys

input = sys.stdin.readline

N = int(input())

spots = [tuple(map(int, input().split())) for _ in range(N)]
spots.sort(key=lambda x: (x[1], x[0]))

for x, y in spots:
    print(x, y)
