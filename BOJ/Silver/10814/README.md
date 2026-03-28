# BOJ 10814 - 나이순 정렬

## 1. 문제 유형
- 정렬 / 문자열 처리

## 2. 처음 접근
- 내장정렬 키를 통한 정렬

## 3. 제출 코드
```python
N = int(input())
people = []
for _ in range(N):
    age, name = input().split()
    people.append([int(age), name])
people.sort(key=lambda x: x[0])

for i in range(N):
    print(people[i][0], people[i][1])
```

## 4. 개선 포인트
- 출력 루프 간소화

## 5. 재작성 코드
```python
import sys
input = sys.stdin.readline

N = int(input())
people = []

for _ in range(N):
    age, name = input().split()
    people.append((int(age), name))

people.sort(key=lambda x: x[0])

for age, name in people:
    print(age, name)
```

## 6. 배운점
- 

## 7. 풀이기록 
- 1차 풀이 : 2026-03-08
- 2차 풀이 : 2026-03-28
