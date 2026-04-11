import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = dp[i - 1] + nums[i]

out = []
for _ in range(M):
    i, j = map(int, input().split())
    out.append(str(dp[j] - dp[i - 1]))

sys.stdout.write("\n".join(out))
