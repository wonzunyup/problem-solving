# BOJ 1003 - 피보나치 함수

## 1. 문제 유형
- DP

## 2. 처음 접근
- DP를 통한 계산

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

T = int(input())

out = []
for _ in range(T):
    N = int(input())
    if N == 0:
        out.append((1, 0))
    elif N == 1:
        out.append((0, 1))
    else:
        dp = [[0, 0] for _ in range(N + 1)]
        dp[0][0], dp[0][1] = 1, 0
        dp[1][0], dp[1][1] = 0, 1
        for i in range(2, N + 1):
            dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
            dp[i][1] = dp[i - 1][1] + dp[i - 2][1]
        out.append((dp[N][0], dp[N][1]))

for i in range(T):
    sys.stdout.write(f"{out[i][0]} {out[i][1]}\n")
```

## 4. 개선 포인트
- dp를 매 시행마다 만들지 말고, 입력값들 중 최대값 기준으로 하나 만들기

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]
max_n = max(nums)

dp = [[0, 0] for _ in range(max_n + 1)]
dp[0] = [1, 0]

if max_n >= 1:
    dp[1] = [0, 1]

for i in range(2, max_n + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

for n in nums:
    sys.stdout.write(f"{dp[n][0]} {dp[n][1]}\n")
```

## 6. 배운점
- dp 여러번 만들지 말고 한번 생성으로 활용

## 7. 풀이기록 
- 1차 풀이 : 2026-04-02
- 2차 풀이 : 2026-04-06
