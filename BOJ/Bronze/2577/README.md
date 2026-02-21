# BOJ 2577 - 숫자의 개수
## 1. 문제 유형
- 구현 / 카운팅

## 2. 처음 접근
- A * B * C 계산 후 문자열 변환
- 빈도 배열

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

ABC = str(A * B * C)
count = [0] * 10
for s in ABC:
    count[int(s)] += 1

for i in range(10):
    sys.stdout.write(str(count[i]) + "\n")

```

## 4. 개선 포인트
- 출력 개수가 적어 굳이 write 쓸 필요 X
- 가독성 면에서 print 권장

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

ABC = str(A * B * C)
count = [0] * 10
for s in ABC:
    count[int(s)] += 1

for i in range(10):
    print(count[i])
```

## 6. 배운점
- 입출력 개수를 고려하여 적절한 입출력 함수 활용

## 7. 풀이기록 
- 1차 풀이 : 2026-02-21
