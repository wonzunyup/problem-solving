N = int(input())

values = [0]
for _ in range(N):
    values.append(int(input()))

dp = [0] * (N + 1)
dp[1] = values[1]
if N >= 2:
    dp[2] = values[2] + values[1]
if N >= 3:
    dp[3] = values[3] + max(values[1], values[2])
if N >= 4:
    for i in range(4, N + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + values[i - 1]) + values[i]

print(dp[N])
