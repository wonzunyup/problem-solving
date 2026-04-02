import sys

input = sys.stdin.readline

T = int(input())

out = []
for _ in range(T):
    N = int(input())
    if N == 0:
        out.append((1, 0))
    elif N == 1:
        out.append((0, 1))
    else:
        dp = [[0, 0] for _ in range(N + 1)]
        dp[0][0], dp[0][1] = 1, 0
        dp[1][0], dp[1][1] = 0, 1
        for i in range(2, N + 1):
            dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
            dp[i][1] = dp[i - 1][1] + dp[i - 2][1]
        out.append((dp[N][0], dp[N][1]))

for i in range(T):
    sys.stdout.write(f"{out[i][0]} {out[i][1]}\n")
