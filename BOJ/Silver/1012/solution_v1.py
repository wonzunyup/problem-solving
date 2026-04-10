import sys
sys.setrecursionlimit(10**6)

def dfs(y, x):
    visited[y][x] = True
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                dfs(ny, nx)


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and not visited[y][x]:
                dfs(y, x)
                count += 1

    print(count)
