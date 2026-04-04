import sys

input = sys.stdin.readline

N = int(input())
times = sorted(map(int, input().split()))

acc = 0
total = 0
for time in times:
    total += time + acc
    acc += time

print(total)
