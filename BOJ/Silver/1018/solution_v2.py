import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]

least = 64
for n in range(N - 7):
    for m in range(M - 7):
        cnt = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if (i + j) % 2 == 0:
                    if board[n + i][m + j] != "B":
                        cnt += 1
                else:
                    if board[n + i][m + j] != "W":
                        cnt += 1
        cnt = min(cnt, 64 - cnt)
        least = min(least, cnt, 64 - cnt)

print(least)
