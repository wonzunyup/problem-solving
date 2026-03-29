# BOJ 18110 - solved.ac

## 1. 문제 유형
- 구현 / 정렬

## 2. 처음 접근
- 리스트 슬라이싱 및 반올림 연산 구현

## 3. 제출 코드
```python
import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
else:
    levels = [int(input()) for _ in range(n)]
    num = int(n * 0.15 + 0.5)

    levels.sort()
    if num > 0:
        levels = levels[num:-num]
    print(int(sum(levels) / len(levels) + 0.5))
```

## 4. 개선 포인트
- 슬라이싱으로 새 리스트 만드는 대신 합 구간만 구함
- 변수명 변경

## 5. 재작성 코드
```python
import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    levels = [int(input()) for _ in range(n)]
    cut = int(n * 0.15 + 0.5)

    levels.sort()

    if cut > 0:
        levels = levels[cut:-cut]

    print(int(sum(levels) / len(levels) + 0.5))
```

## 6. 배운점
- 리스트 슬라이싱은 새로운 리스트를 만드므로 효율 저하

## 7. 풀이기록 
- 1차 풀이 : 2026-03-17
- 2차 풀이 : 2026-03-29
