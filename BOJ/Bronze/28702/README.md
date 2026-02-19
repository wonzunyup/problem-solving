# BOJ 28702 - FizzBuzz

## 1. 문제 유형
- 구현 / 문자열 처리

## 2. 처음 접근
- 숫자 위치 찾아서 다음 문자열 예측

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

strings = [input().strip() for _ in range(3)]
pos = 0
for i in range(3):
    if strings[i] == "Fizz" or strings[i] == "Buzz" or strings[i] == "FizzBuzz":
        continue
    else:
        pos = i

num = int(strings[pos]) + 3 - pos
if num % 3 == 0:
    if num % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    if num % 5 == 0:
        print("Buzz")
    else:
        print(num)
```

## 4. 개선 포인트
- 내장함수 isdigit() 활용
- 출력 로직 단순화

## 5. 재작성 코드
```python
import sys
input = sys.stdin.readline

strings = [input().strip() for _ in range(3)]

pos = -1
for i in range(3):
    if strings[i].isdigit():
        pos = i
        break

num = int(strings[pos]) + (3 - pos)

if num % 15 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
```

## 6. 배운점
- 파이썬의 다양한 내장함수를 활용하여 최적화된 풀이
- 출력 조건문 단순화

## 7. 풀이기록 
- 1차 풀이 : 2026-02-19
