# BOJ 9012 - 괄호

## 1. 문제 유형
- 자료구조(stack)

## 2. 처음 접근
- stack을 활용한 괄호검사

## 3. 제출 코드
```python
import sys
input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    string = input().rstrip()
    stack = []

    for ch in string:
        if ch == "(":
            stack.append(ch)
        else:
            if not stack:
                out.append("NO")
                break
            stack.pop()
    else:
        out.append("YES" if not stack else "NO")

sys.stdout.write("\n".join(out))
```

## 4. 개선 포인트
- X

## 5. 풀이기록 
- 1차 풀이 : 2026-03-15
- 2차 풀이 : 2026-03-29
