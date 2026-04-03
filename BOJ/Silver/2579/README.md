# BOJ 2579 - 계단 오르기

## 1. 문제 유형
- DP

## 2. 처음 접근
- i번째 계단에 접근할 때 오는 방법을 i-2를 거치고 오는 방법과 i-3, i-1을 거치고 오는 방법으로 분리

## 3. 제출 코드
```python
N = int(input())

values = [0]
for _ in range(N):
    values.append(int(input()))

dp = [0] * (N + 1)
dp[1] = values[1]
if N >= 2:
    dp[2] = values[2] + values[1]
if N >= 3:
    dp[3] = values[3] + max(values[1], values[2])
if N >= 4:
    for i in range(4, N + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + values[i - 1]) + values[i]

print(dp[N])
```

## 4. 개선 포인트
- 코드 간소화

## 5. 재작성 코드
```python
N = int(input())
values = [0] + [int(input()) for _ in range(N)]

dp = [0] * (N + 1)
dp[1] = values[1]

if N >= 2:
    dp[2] = values[1] + values[2]
if N >= 3:
    dp[3] = max(values[1], values[2]) + values[3]

for i in range(4, N + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + values[i - 1]) + values[i]

print(dp[N])
```

## 6. 배운점
- N이 작을 때 인덱스 접근 에러가 나지 않게 N 값 범위에 따른 처리 신경쓰기

## 7. 풀이기록 
- 1차 풀이 : 2026-04-03
