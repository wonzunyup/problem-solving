# BOJ 11650 - 좌표 정렬하기

## 1. 문제 유형
- 정렬

## 2. 처음 접근
- 리스트를 다중 키 정렬

## 3. 제출 코드
```python
import sys
input = sys.stdin.readline

N = int(input())

spots = [list(map(int, input().split())) for _ in range(N)]
spots.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    sys.stdout.write(str(spots[i][0]) + " " + str(spots[i][1]) + "\n")
```

## 4. 개선 포인트
- 좌표는 변경되지 않으므로 튜플 이용 -> 메모리 조금 절약, 의미적으로 자연스러움
- 출력 루프 간단화 : 입력이 10만이라 print도 충분히 통과

## 5. 재작성 코드
```python
import sys
input = sys.stdin.readline

N = int(input())

spots = [tuple(map(int, input().split())) for _ in range(N)]
spots.sort()

for x, y in spots:
    print(x, y)
```

## 6. 배운점
- 튜플 정렬은 자동으로 (x1, y1) < (x2, y2) 순으로 비교함

## 7. 풀이기록 
- 1차 풀이 : 2026-03-09
