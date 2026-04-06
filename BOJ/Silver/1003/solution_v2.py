import sys

input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]

max_num = max(nums)
dp = [[0, 0] for _ in range(max_num + 1)]
dp[0] = [1, 0]
if max_num >= 1:
    dp[1] = [0, 1]
for i in range(2, max_num + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]


for num in nums:
    sys.stdout.write(f"{dp[num][0]} {dp[num][1]}\n")
