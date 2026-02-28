import sys

input = sys.stdin.readline

N = int(input())
cnt = [0] * 10001

for _ in range(N):
    cnt[int(input())] += 1

for x in range(1, 10001):
    if cnt[x]:
        sys.stdout.write((str(x) + "\n") * cnt[x])
