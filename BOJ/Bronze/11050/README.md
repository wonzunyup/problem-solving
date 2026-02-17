# BOJ 11050 - 이항 계수 1

## 1. 문제 유형
- 조합 / DP

## 2. 처음 접근
- DP 

## 3. 제출 코드
```python
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = 1
    dp[i][i] = 1

for i in range(1, N + 1):
    for j in range(0, K + 1):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

sys.stdout.write(str(dp[N][K]))
```

## 4. 개선 포인트
- 인덱스 범위를 보수적으로 적용, 불필요한 범위 계산 x, N의 개수가 작으므로 팩토리얼이 효율적

## 5. 재작성 코드
```python
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = 1
    dp[i][i] = 1

for i in range(1, N + 1):
    for j in range(1, min(i, K) + 1):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

sys.stdout.write(str(dp[N][K]))
```
```python
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def fact(x):
    r = 1
    for i in range(2, x + 1):
        r *= i
    return r

print(fact(N) // (fact(K) * fact(N - K)))

```

## 6. 배운점
- 불필요한 범위의 연산을 최소화
- 인덱스 접근 시 오류 가능성 체크
- N의 개수에 따른 코드 효율성 체크

## 7. 풀이기록 
- 1차 풀이 : 2026-02-17
