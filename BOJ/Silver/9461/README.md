# BOJ 9461 - 파도반 수열

## 1. 문제 유형
- DP

## 2. 처음 접근
- dp[n] = dp[n-2] + dp[n-3] 로 점화식 구성

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

T = int(input())
N = [int(input()) for _ in range(T)]
max_n = max(N)

dp = [0] * (max_n + 1)
dp[1] = 1
if max_n >= 2:
    dp[2] = 1
if max_n >= 3:
    dp[3] = 1
for i in range(4, max_n + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

sys.stdout.write("\n".join(map(str, [dp[n] for n in N])))

```

## 4. 개선 포인트
- 조건문 대신 배열 크기를 넉넉히 잡는 안정적인 방법

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]
max_n = max(nums)

dp = [0] * (max(4, max_n) + 1)
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, max_n + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

sys.stdout.write("\n".join(str(dp[n]) for n in nums))
```

## 6. 배운점
- X

## 7. 풀이기록 
- 1차 풀이 : 2026-04-08
