import sys

input = sys.stdin.readline

N = int(input())
network = [[] for _ in range(N + 1)]

M = int(input())
for _ in range(M):
    com1, com2 = map(int, input().split())
    network[com1].append(com2)
    network[com2].append(com1)

visited = [False] * (N + 1)


def dfs(v):
    visited[v] = True
    for nxt in network[v]:
        if not visited[nxt]:
            dfs(nxt)


dfs(1)
print(sum(visited) - 1)
