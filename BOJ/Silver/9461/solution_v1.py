import sys

input = sys.stdin.readline

T = int(input())
N = [int(input()) for _ in range(T)]
max_n = max(N)

dp = [0] * (max_n + 1)
dp[1] = 1
if max_n >= 2:
    dp[2] = 1
if max_n >= 3:
    dp[3] = 1
for i in range(4, max_n + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

sys.stdout.write("\n".join(map(str, [dp[n] for n in N])))
