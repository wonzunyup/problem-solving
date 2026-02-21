# BOJ 10250 - ACM 호텔

## 1. 문제 유형
- 구현 / 수학

## 2. 처음 접근
- 올림 나눗셈을 통한 연산 구현

## 3. 제출 코드
```python
import sys
input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    H, W, N = map(int, input().split())
    num = (N + H - 1) // H
    floor = N % H
    if floor == 0:
        floor = H
    out.append(str(floor) + "0" + str(num) + "\n")

sys.stdout.write("".join(out))
```

## 4. 개선 포인트
- 문자열 출력 방식 오류
- 0을 항상 추가하여 34호가 배정될 경우에도 12034와 같이 출력되는 문제
- 문자열 포매팅 사용

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    H, W, N = map(int, input().split())
    room = (N + H - 1) // H
    floor = N % H
    if floor == 0:
        floor = H
    out.append(f"{floor}{room:02d}\n")

sys.stdout.write("".join(out))
```

## 6. 배운점
- 문제 틀렸을 시 출력 방식 점검해보기

## 7. 풀이기록 
- 1차 풀이 : 2026-02-21
