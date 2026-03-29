# BOJ 10816 - 숫자 카드 2

## 1. 문제 유형
- 해시 / 빈도수 카운팅

## 2. 처음 접근
- counter를 통한 숫자 개수 카운팅

## 3. 제출 코드
```python
import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())
nums = list(map(int, input().split()))
c = Counter(nums)

out = []
M = int(input())
for num in map(int, input().split()):
    out.append(str(c[num]))

sys.stdout.write(" ".join(out))
```

## 4. 개선 포인트
- 코드 간소화, 필요 없는 값 변수 할당 X

## 5. 재작성 코드
```python
import sys
input = sys.stdin.readline

from collections import Counter

input()
c = Counter(map(int, input().split()))

input()
out = []
for num in map(int, input().split()):
    out.append(str(c[num]))

sys.stdout.write(" ".join(out))
```

## 6. 배운점
- 매 반복마다 리스트르 순회하는 것이 아닌, 빈도 수를 순회 한번으로 저장하여 접근
- counter 활용

## 7. 풀이기록 
- 1차 풀이 : 2026-03-16
- 2차 풀이 : 2026-03-29
