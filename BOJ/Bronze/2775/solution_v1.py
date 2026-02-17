import sys
input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    k = int(input())
    n = int(input())
    dp = [[0] * (n + 1)] * (k + 1)
    for i in range(n + 1):
        dp[0][i] = i
    for i in range(k + 1):
        dp[i][1] = 1
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    out.append(str(dp[k][n]) + "\n")

sys.stdout.write("".join(out))
