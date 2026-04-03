N = int(input())
graph = [[] for _ in range(N + 1)]

M = int(input())
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

visited = [False] * (N + 1)

def dfs(v):
    visited[v] = True
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt)

dfs(1)

cnt = 0
for v in visited:
    if v:
        cnt += 1

print(cnt - 1)
