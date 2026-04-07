# BOJ 9095 - 1, 2, 3 더하기

## 1. 문제 유형
- DP

## 2. 처음 접근
- i-3에서 3을 더하는 경우, i-2에서 2를 더하는 경우, i-1에서 1을 더하는 경우로 계산 

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]

max_n = max(nums)
dp = [0] * (max_n + 1)
if max_n >= 1:
    dp[1] = 1
if max_n >= 2:
    dp[2] = 2
if max_n >= 3:
    dp[3] = 4

for i in range(4, max_n + 1):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

out = []
for n in nums:
    out.append(str(dp[n]))

sys.stdout.write("\n".join(out))

```

## 4. 개선 포인트
- X

## 5. 풀이기록 
- 1차 풀이 : 2026-04-07 
