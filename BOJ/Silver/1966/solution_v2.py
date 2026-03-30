from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))

    q = deque((i, p) for i, p in enumerate(priorities))

    cnt = [0] * 10
    for p in priorities:
        cnt[p] += 1

    cur_max = 9
    while cnt[cur_max] == 0:
        cur_max -= 1

    order = 0
    while q:
        idx, priority = q.popleft()
        if priority == cur_max:
            order += 1
            cnt[cur_max] -= 1

            if idx == M:
                print(order)
                break

            while cur_max > 0 and cnt[cur_max] == 0:
                cur_max -= 1
        else:
            q.append((idx, priority))
