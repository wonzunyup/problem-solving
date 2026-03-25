from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))

    q = deque((i, priorities[i]) for i in range(N))

    cnt = 0

    while q:
        idx, priority = q.popleft()

        if any(priority < x[1] for x in q):
            q.append((idx, priority))
        else:
            cnt += 1
            if idx == M:
                print(cnt)
                break
