# BOJ 11727 - 2xn 타일링 2

## 1. 문제 유형
- DP

## 2. 처음 접근
- 점화식을 통한 계산

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (max(2, n) + 1)
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (2 * dp[i - 2] + dp[i - 1]) % 10007

print(dp[n])

```

## 4. 개선 포인트
- X

## 5. 풀이기록 
- 1차 풀이 : 2026-04-09
