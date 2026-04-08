# BOJ 11659 - 구간 합 구하기 4

## 1. 문제 유형
- 누적합

## 2. 처음 접근
- 

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)
dp[1] = nums[1]

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + nums[i]

out = []
for _ in range(M):
    i, j = map(int, input().split())
    out.append(dp[j] - dp[i - 1])

sys.stdout.write("\n".join(map(str, out)))

```

## 4. 개선 포인트
- 초기값이 0이라 dp[1] 초기화 없이 가능

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = dp[i - 1] + nums[i]

out = []
for _ in range(M):
    i, j = map(int, input().split())
    out.append(dp[j] - dp[i - 1])

sys.stdout.write("\n".join(map(str, out)))
```

## 6. 배운점
- 초기값 설정 생각 잘하기

## 7. 풀이기록 
- 1차 풀이 : 2026-04-09
