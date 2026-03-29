# BOJ 11866 - 요세푸스 문제 0

## 1. 문제 유형
- 자료구조(deque)

## 2. 처음 접근
- 덱을 rotate하여 K번째 원소 popleft

## 3. 제출 코드
```python
from collections import deque

N, K = map(int, input().split())

nums = deque(i for i in range(1, N + 1))
josephus = []

for _ in range(N):
    nums.rotate(-(K - 1))
    josephus.append(nums.popleft())

print("<" + ", ".join(map(str, josephus)) + ">")
```

## 4. 개선 포인트
- X

## 5. 풀이기록 
- 1차 풀이 : 2026-03-17
- 2차 풀이 : 2026-03-29
