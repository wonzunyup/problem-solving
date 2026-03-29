# BOJ 4949 - 균형잡힌 세상 

## 1. 문제 유형
- 자료구조(stack)

## 2. 처음 접근
- stack과 검사 조건을 통해 괄호쌍 판별

## 3. 제출 코드
```python
import sys
input = sys.stdin.readline

out = []
while True:
    string = input().rstrip()
    if string == ".":
        break
    stack = []

    for ch in string:
        if ch == "[" or ch == "(":
            stack.append(ch)
        elif ch == "]":
            if not stack or stack.pop() != "[":
                out.append("no")
                break
        elif ch == ")":
            if not stack or stack.pop() != "(":
                out.append("no")
                break
        else:
            continue
    else:
        if stack:
            out.append("no")
        else:
            out.append("yes")

sys.stdout.write("\n".join(out))
```

## 4. 개선 포인트
- 파이썬 문법을 통한 코드 간소화

## 5. 재작성 코드
```python
import sys
input = sys.stdin.readline

out = []
while True:
    string = input().rstrip()
    if string == ".":
        break
    stack = []

    for ch in string:
        if ch in "([" :
            stack.append(ch)
        elif ch == "]":
            if not stack or stack.pop() != "[":
                out.append("no")
                break
        elif ch == ")":
            if not stack or stack.pop() != "(":
                out.append("no")
                break
        else:
            continue
    else:
        if stack:
            out.append("no")
        else:
            out.append("yes")

sys.stdout.write("\n".join(out))
```

## 6. 배운점
- 파이썬 문법 활용

## 7. 풀이기록 
- 1차 풀이 : 2026-03-15
- 2차 풀이 : 2026-03-29
