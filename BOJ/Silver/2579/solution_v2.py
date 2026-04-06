import sys

input = sys.stdin.readline

N = int(input())

values = [0] + [int(input()) for _ in range(N)]

dp = [0] * (N + 1)
dp[1] = values[1]
if N >= 2:
    dp[2] = values[1] + values[2]
if N >= 3:
    dp[3] = max(values[1], values[2]) + values[3]

for i in range(4, N + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + values[i - 1]) + values[i]

print(dp[N])
