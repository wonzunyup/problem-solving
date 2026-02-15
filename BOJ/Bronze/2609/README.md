# BOJ 2609 - 최대공약수와 최대공배수

## 1. 문제 유형
- 구현

## 2. 처음 접근
- 공식 활용

## 3. 제출 코드
```python
n1, n2 = map(int, input().split())

a, b = n1, n2
while b:
    a, b = b, a % b

gcd = a
lcm = n1 * n2 // gcd

print(gcd)
print(lcm)
```

## 4. 배운점
- 간단 구현은 기본 공식 활용

## 5. 풀이기록 
- 1차 풀이 : 2026-02-15
