# BOJ 2108 - 통계학

## 1. 문제 유형
- 구현 / 정렬 / 빈도수 처리

## 2. 처음 접근
- 평균 : 직접 계산, 중앙값 : 인덱스 접근, 최빈값 : counter 활용, 범위 : 직접 계산

## 3. 제출 코드
```python
from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]
nums.sort()

total = sum(nums)
if total >= 0:
    mean = int((total / N) + 0.5)
else:
    mean = int((total / N) - 0.5)
print(mean)

median = nums[N // 2]
print(median)

commons = Counter(nums).most_common()
modes = []
for i in range(len(commons)):
    if commons[i][1] == commons[0][1]:
        modes.append(commons[i][0])
modes.sort()
if len(modes) >= 2:
    mode = modes[1]
else:
    mode = modes[0]
print(mode)

ran = nums[-1] - nums[0]
print(ran)
```

## 4. 개선 포인트
- 최빈값 처리 개선
- 직접 순회 활용

## 5. 재작성 코드
```python
from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

total = sum(nums)
if total >= 0:
    mean = int(total / N + 0.5)
else:
    mean = int(total / N - 0.5)
print(mean)

print(nums[N // 2])

counter = Counter(nums)
max_freq = max(counter.values())
modes = [num for num, freq in counter.items() if freq == max_freq]
modes.sort()
print(modes[1] if len(modes) > 1 else modes[0])

print(nums[-1] - nums[0])
```

## 6. 배운점
- 라이브러리 결과 그대로 활용보다 문제 조건이 요구하는 정렬 다시 맞추기
- 인덱스 순회보다 직접 순회하기

## 7. 풀이기록 
- 1차 풀이 : 2026-03-26
- 2차 풀이 : 2026-03-30
