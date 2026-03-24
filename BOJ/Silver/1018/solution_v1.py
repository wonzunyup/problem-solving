import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(input().strip())

least = 64

for n in range(N - 7):
    for m in range(M - 7):
        start = board[n][m]
        cnt = 0

        for i in range(n, n + 8):
            for j in range(m, m + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] != start:
                        cnt += 1
                else:
                    if board[i][j] == start:
                        cnt += 1

        least = min(least, cnt, 64 - cnt)

print(least)
