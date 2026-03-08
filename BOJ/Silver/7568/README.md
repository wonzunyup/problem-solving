# BOJ 7568 - 덩치

## 1. 문제 유형
- 브루트포스 / 구현

## 2. 처음 접근
- 본인보다 덩치가 큰 사람이 있으면 덩치 + 1

## 3. 제출 코드
```python
import sys
input = sys.stdin.readline

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    rank = 1
    for j in range(N):
        if j != i:
            if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
                rank += 1
    print(rank, end = " ")
```

## 4. 개선 포인트
- if j != i는 다음 조건문이 참일 시 무조건 참이므로 불필요한 조건문

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    rank = 1
    for j in range(N):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    print(rank, end=" ")
```

## 6. 배운점
- 불필요한 정렬 없이 전체 원소를 직접 비교도 필요

## 7. 풀이기록 
- 1차 풀이 : 2026-03-08
