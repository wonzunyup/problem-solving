# BOJ 1463 - 1로 만들기

## 1. 문제 유형
- DP

## 2. 처음 접근
- DP를 통해 2의 배수인 경우, 3의 배수인경우, 이전 단계에서 1 더하는 경우를 비교

## 3. 제출 코드
```python
N = int(input())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[N])

```

## 4. 개선 포인트
- X

## 5. 풀이기록 
- 1차 풀이 : 2026-04-02 
