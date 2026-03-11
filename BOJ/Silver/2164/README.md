# BOJ 2164 - 카드2

## 1. 문제 유형
- 자료구조(deque)

## 2. 처음 접근
- deque를 활용하여 문제 풀이

## 3. 제출 코드
```python
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
nums = deque([i for i in range(1, N + 1)])

while len(nums) > 1:
    nums.popleft()
    nums.append(nums[0])
    nums.popleft()

print(nums[0])
```

## 4. 개선 포인트
- deque 사용의 미숙한 부분 개선

## 5. 재작성 코드
```python
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
nums = deque(range(1, N+1))

while len(nums) > 1:
    nums.popleft()
    nums.append(nums.popleft())

print(nums[0])
```

## 6. 배운점
- 수학적인 원리로 상수 시간에 풀이 할 수 있지만

## 7. 풀이기록 
- 1차 풀이 : 2026-03-11
