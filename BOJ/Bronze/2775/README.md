# BOJ 2775 - 부녀회장이 될테야

## 1. 문제 유형
- DP(동적 계획법)

## 2. 처음 접근
- 점화식을 통한 DP 

## 3. 제출 코드
```python
import sys
input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    k = int(input())
    n = int(input())
    dp = [[0] * (n + 1)] * (k + 1)
    for i in range(n + 1):
        dp[0][i] = i
    for i in range(k + 1):
        dp[i][1] = 1
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    out.append(str(dp[k][n]) + "\n")

sys.stdout.write("".join(out))
```

## 4. 개선 포인트
-  dp = [[0] * (n + 1)] * (k + 1) 버그 가능성
-  필요 없는 초기화 삭제

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    k = int(input())
    n = int(input())

    dp = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(n + 1):
        dp[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    out.append(str(dp[k][n]) + "\n")

sys.stdout.write("".join(out))
```

## 6. 배운점
- DP를 학교 알고리즘 수업시간 때 접해보지 못해 처음 개념을 공부하고 문제 풀이에 적용해보았는데 앞으로 내가 가져가야할 중요한 개념 중 하나라는 생각이 들었고 더 많은 case를 통해 활용해보아야겠다.
- 불필요한 초기화 X

## 7. 풀이기록 
- 1차 풀이 : 2026-02-16
- 2차 풀이 : 2026-02-28


