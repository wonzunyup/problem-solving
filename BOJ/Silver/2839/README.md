# BOJ 2839 - 설탕 배달

## 1. 문제 유형
- 그리디 / 브루트포스

## 2. 처음 접근
- 5의 개수를 0 부터 시작해서 나머지가 3으로 나누어 떨어지면 봉투 개수 갱신

## 3. 제출 코드
```python
N = int(input())

least = -1
five = 0

while 5 * five <= N:
    count = five
    temp = N
    temp -= 5 * five
    if temp % 3 == 0:
        count += temp // 3
        least = count
    five += 1

print(least)
```

## 4. 개선 포인트
- 5kg을 많이 쓸수록 최소 봉투 개수가 되므로 그리디를 통한 풀이가 적합

## 5. 재작성 코드
```python
N = int(input())

for five in range(N // 5, -1, -1) :
    remain = N - 5 * five
    if remain % 3 == 0 :
        print(five + remain // 3)
        break

else : 
    print(-1)
```

## 6. 배운점
- 최소 / 최대 + 선택 문제의 경우 그리디를 통한 풀이가 효과적
- 핵심은 현재 가장 좋은 선택을 해도 이후에 영향을 안주는가 확인
- 예로 동전 문제의 경우 500원을 먼저 써도 이후에 100원, 50원을 쓸때 최적해가 깨지지 않음

## 7. 풀이기록 
- 1차 풀이 : 2023-03-11
