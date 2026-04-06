# BOJ 2606 - 바이러스

## 1. 문제 유형
- 그래프 탐색(DFS/BFS)

## 2. 처음 접근
- DFS 활용

## 3. 제출 코드
```python
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
```

## 4. 개선 포인트
- 파이썬에서 True가 1로 취급되는 점을 이용해 cnt 계산 없이 간소화

## 5. 재작성 코드
```python
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

print(sum(visited) - 1)
```

## 6. 배운점
- X

## 7. 풀이기록 
- 1차 풀이 : 2026-04-03
- 2차 풀이 : 2026-04-06
