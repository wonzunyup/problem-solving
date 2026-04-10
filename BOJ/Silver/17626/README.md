# BOJ 17626 - Four Squares

## 1. 문제 유형
- DP / 수학 구현

## 2. 처음 접근
- DP를 통한 구현

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = i
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[n])
```

## 4. 개선 포인트
- 해당 코드도 로직은 맞으나 python3의 경우 시간 초과가 날 우려 있음

## 5. 재작성 코드
```python
import sys
import math

input = sys.stdin.readline

n = int(input())

if int(math.isqrt(n)) ** 2 == n:
    print(1)
    sys.exit()

for i in range(1, math.isqrt(n) + 1):
    remain = n - i * i
    if int(math.isqrt(remain)) ** 2 == remain:
        print(2)
        sys.exit()

x = n
while x % 4 == 0:
    x //= 4

if x % 8 == 7:
    print(4)
else:
    print(3)
```

## 6. 배운점
- 가끔 이런 특이한 수학 패턴이 나오는 경우도 있음
- 이런 경우 일반적인 DP 방법을 통한 풀이는 시간 초과에 걸릴 수도 있

## 7. 풀이기록 
- 1차 풀이 : 2026-04-10
