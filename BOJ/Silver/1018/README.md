# BOJ 1018 - 체스판 다시 칠하기

## 1. 문제 유형
- 브루트포스 / 구현

## 2. 처음 접근
- 전체 입력중 8*8 칸을 잘라서 검사
- B, W로 시작하는 경우 두 부분 중 최소값을 출력

## 3. 제출 코드
```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(input().strip())

least = 64

for n in range(N - 7):
    for m in range(M - 7):
        start = board[n][m]
        cnt = 0

        for i in range(n, n + 8):
            for j in range(m, m + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] != start:
                        cnt += 1
                else:
                    if board[i][j] == start:
                        cnt += 1

        least = min(least, cnt, 64 - cnt)

print(least)
```

## 4. 개선 포인트
- X

## 5. 배운점
- 패턴 찾아내는 연습 필요
- 가능한 경우의 수 모두 생각

## 7. 풀이기록 
- 1차 풀이 : 2026-03-24
- 2차 풀이 : 2026-03-30
