# BOJ 15829 - Hashing

## 1. 문제 유형
- 해시 함수 구현

## 2. 처음 접근
- 연산 구현

## 3. 제출 코드
```python
L = int(input())
string = input()
hash = 0

for i in range(L) :
  hash += ((ord(string[i]) - 96) * (31 ** i))
hash %=1234567891

print(hash)
```

## 4. 개선 포인트
- 모듈러 연산 안정성
- 상수 선언

## 5. 재작성 코드
```python
MOD = 1234567891
r = 31

L = int(input())
string = input()
hash_val = 0
power = 1

for ch in string :
  hash_val += ((ord(ch) - 96) * power) % MOD
  power = (power * r) % MOD

print(hash_val)
```

## 6. 배운점
- 큰 수에 직접 곱하는 연산이 누적될 수록 연산 부담이 커질 수 있으니 고려 필요

## 7. 풀이기록 
- 1차 풀이 : 2026-02-15
- 2차 풀이 : 2026-02-24
