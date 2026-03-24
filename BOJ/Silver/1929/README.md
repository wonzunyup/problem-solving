# BOJ 1929 - 소수 구하기

## 1. 문제 유형
- 수학

## 2. 처음 접근
- 에라토스테네스의 체를 통한 소수 판정

## 3. 제출 코드
```python
import sys

M, N = map(int, input().split())

is_prime = [True] * (N + 1)
if N >= 0:
    is_prime[0] = False
if N >= 1:
    is_prime[1] = False

for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

primes = [i for i in range(M, N + 1) if is_prime[i]]
sys.stdout.write("\n".join(map(str, primes)))
```

## 4. 개선 포인트
- X

## 5. 배운점
- 수학 아이디어를 구현으로 옮길 수 있게 체화 필요

## 7. 풀이기록 
- 1차 풀이 : 2026-03-24
