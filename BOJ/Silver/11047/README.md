# BOJ 11047 - 동전 0

## 1. 문제 유형
- 그리디

## 2. 처음 접근
- 그리디를 통해 가장 큰 동전부터 계산

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
values = [int(input()) for _ in range(N)]

least = 0
for i in range(len(values) - 1, -1, -1):
    least += K // values[i]
    K %= values[i]
print(least)

```

## 4. 개선 포인트
- 인덱스가 아닌 직접 순회를 통한 코드 직관성 향상

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
values = [int(input()) for _ in range(N)]

count = 0
for coin in reversed(values):
    count += K // coin
    K %= coin

print(count)

```

## 6. 배운점
- 직접 순회 활용

## 7. 풀이기록 
- 1차 풀이 : 2026-04-01
- 2차 풀이 : 2026-04-04
