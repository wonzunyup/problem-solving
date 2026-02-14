# BOJ 2231 분해합

## 1. 문제 유형
- 브루트포스

## 2. 처음 접근
- 각 자리수의 합을 통한 분해자 계산

## 3. 제출 코드
```python
N = int(input())

generator = 0
for i in range(N, 0, -1) :
  sum = i
  temp = str(i)
  for j in range(len(temp)) :
    sum += int(temp[len(temp) - 1 - j])
  if sum == N : generator = i
print(generator)
```

## 4. 개선 포인트
- 변수명 파이썬 내장 함수와 충돌, 자리수 더하는 계산 간소화, 탐색 범위 축소

## 5. 재작성 코드
```python
N = int(input())

generator = 0
start = max(0, N - 9 * len(str(N)))

for i in range(start, N) :
  total = i
  for digit in str(i) :
    total += int(digit)
  if total == N :
    generator = i
    break

print(generator)
```

## 6. 배운점
- 변수명 충돌 고려, 계산 간소화, 탐색 유형 분석(브루트포스), 구현 시 탐색범위 최소화 고려

## 7. 풀이기록 
- 1차 풀이 : 2026-02-14
