# BOJ 11399 - ATM

## 1. 문제 유형
- 그리디 / 누적합

## 2. 처음 접근
- 누적 합을 통한 시간 계산

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
times.sort()

total = 0
acc = 0
for time in times:
    total += acc + time
    acc += time
    
sys.stdout.write(str(total))

```

## 4. 개선 포인트
- sorted를 통해 한번에 정렬 리스트 생성
- N 사용 안하므로 버려도 됨

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

input()
times = sorted(map(int, input().split()))


total = 0
acc = 0
for time in times:
    total += acc + time
    acc += time

sys.stdout.write(str(total))
```

## 6. 배운점
- X

## 7. 풀이기록 
- 1차 풀이 : 2026-04-01
- 2차 풀이 : 2026-04-04
