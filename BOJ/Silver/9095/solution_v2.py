import sys

input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]
max_n = max(nums)

dp = [0] * (max(2, max_n) + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

sys.stdout.write("\n".join(str(dp[n]) for n in nums))
