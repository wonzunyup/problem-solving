# BOJ 11651 - 좌표 정렬하기 2

## 1. 문제 유형
- 정렬

## 2. 처음 접근
- 다중 키 정렬

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

N = int(input())

spots = [tuple(map(int, input().split())) for _ in range(N)]
spots.sort(key=lambda x: (x[1], x[0]))

for x, y in spots:
    print(x, y)
```

## 4. 개선 포인트
- X

## 5. 배운점
- X

## 6. 풀이기록 
- 1차 풀이 : 2023-03-09
- 2차 풀이 : 2023-03-28
