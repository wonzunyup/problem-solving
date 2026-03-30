# BOJ 1966 - 프린터 큐

## 1. 문제 유형
- 큐 시뮬레이션 

## 2. 처음 접근
- any를 통한 중요도 판정

## 3. 제출 코드
```python
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
```

## 4. 개선 포인트
- 큐 생성 간단화
- 중요도 범위가 0~9 이므로 카운트 배열로 관리

## 5. 재작성 코드
```python
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

    printed = 0

    while q:
        idx, priority = q.popleft()

        if priority == cur_max:
            printed += 1
            cnt[cur_max] -= 1

            if idx == M:
                print(printed)
                break

            while cur_max > 0 and cnt[cur_max] == 0:
                cur_max -= 1
        else:
            q.append((idx, priority))
```

## 6. 배운점
- any는 복잡도가 O(n)이므로 해당 문제에서는 문제 없지만 다른 효율적인 해결책 존재
- 수의 범위가 작은 경우 count 배열, 정렬 적극 활용

## 7. 풀이기록 
- 1차 풀이 : 2026-03-26
- 2차 풀이 : 2026-03-30
