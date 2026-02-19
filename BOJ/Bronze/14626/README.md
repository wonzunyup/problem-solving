# BOJ 14626 - ISBN

## 1. 문제 유형
- 구현 / 문자열 처리

## 2. 처음 접근
- 수식 구현 

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline
ISBN = input()
m = int(ISBN[12])

total = 0
for i in range(12):
    if ISBN[i] == "*":
        continue
    if i % 2 == 0:
        total += int(ISBN[i])
    else:
        total += 3 * int(ISBN[i])

pos = ISBN.find("*")
num = 0
while True:
    if pos % 2 == 0 and m == 10 - (total + num) % 10:
        break
    elif pos % 2 == 1 and m == 10 - (total + 3 * num) % 10:
        break
    else:
        num += 1
print(num)
```

## 4. 개선 포인트
- 시간 초과 -> 무한루프 가능성 존재
- 검사 범위 수정 : 0 ~ 9 범위만 확인해도 됨
- 모듈러 연산 잘못 적용 -> 0 일 때 10 으로 판단
- 개행 제거

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

ISBN = input().strip()
m = int(ISBN[12])

total = 0
pos = ISBN.find("*")

for i in range(12):
    if ISBN[i] == "*":
        continue
    w = 1 if i % 2 == 0 else 3
    total += w * int(ISBN[i])

w_missing = 1 if pos % 2 == 0 else 3
for num in range(10):
    temp = total + w_missing * num
    if m == (10 - (temp % 10)) % 10:
        print(num)
        break
```

## 6. 배운점
- 검사 범위 줄이기 *중요*
- 연산을 구현할 때 오류 가능성 체크하기

## 7. 풀이기록 
- 1차 풀이 : 2026-02-19
