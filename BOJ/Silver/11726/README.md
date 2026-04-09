# BOJ 11726 - 2xn 타일

## 1. 문제 유형
- DP

## 2. 처음 접근
- 중복순열을 통한 계산

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

n = int(input())


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


cnt = 0
if n % 2 == 0:
    for i in range(0, n + 1, 2):
        two_by_one = i
        one_by_two = (n - i) // 2
        cnt += factorial(two_by_one + one_by_two) // (
            factorial(one_by_two) * factorial(two_by_one)
        )
else:
    for i in range(1, n + 1, 2):
        two_by_one = i
        one_by_two = (n - i) // 2
        cnt += factorial(two_by_one + one_by_two) // (
            factorial(one_by_two) * factorial(two_by_one)
        )
print(cnt % 10007)
```

## 4. 개선 포인트
- 팩토리얼 계산 반복을 통한 overhead증가 -> dp를 통한 풀이

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (max(2, n) + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 10007

print(dp[n])
```

## 6. 배운점
- 점화식 생각 한번 더해보기

## 7. 풀이기록 
- 1차 풀이 : 2026-04-09
