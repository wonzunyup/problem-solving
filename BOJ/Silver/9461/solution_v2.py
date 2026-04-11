import sys

input = sys.stdin.readline

T = int(input())

nums = [int(input()) for _ in range(T)]
max_n = max(nums)

dp = [1] * (max(3, max_n) + 1)
for i in range(4, max_n + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

sys.stdout.write("\n".join(str(dp[n]) for n in nums))
