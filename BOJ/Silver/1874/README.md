# BOJ 1874 - 스택 수열

## 1. 문제 유형
- 스택 시뮬레이션

## 2. 처음 접근
- 스택의 top이 얻어야 하는 수와 같을 때 까지 push후 pop
- 넣는 수가 n을 넘어 갈 시 불가능 판정

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

n = int(input())
seq = [int(input()) for _ in range(n)]

s = []
check = 0
cur = 1

out = []
for i in seq:
    if not s or s[-1] != i:
        s.append(cur)
        out.append("+")
        cur += 1
        while s[-1] != i:
            s.append(cur)
            out.append("+")
            cur += 1
            if cur > n + 1:
                check = 1
                break
    if check == 1:
        print("NO")
        break
    if s[-1] == i:
        s.pop()
        out.append("-")
else:
    sys.stdout.write("\n".join(out))
```

## 4. 개선 포인트
- 코드 불필요하게 복잡
- 실패 조건 판정 부자연
- while 조건식 위험 가능성

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

n = int(input())
stack = []
out = []
cur = 1

for _ in range(n):
    target = int(input())

    while cur <= target:
        stack.append(cur)
        out.append("+")
        cur += 1

    if stack and stack[-1] == target:
        stack.pop()
        out.append("-")
    else:
        print("NO")
        break
else:
    sys.stdout.write("\n".join(out))

```

## 6. 배운점
- 억지 조건이 아닌 진짜 실패 지점 파악
- while 문에서 push 두번 한거 같이 구현 말고 같은 규칙을 한덩어리로 묶기
- 불필요한 플래그 변수 지양

## 7. 풀이기록 
- 1차 풀이 : 2026-03-26
- 2차 풀이 : 2026-03-30
