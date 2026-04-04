# BOJ 11723 - 집합

## 1. 문제 유형
- 자료구조(set)

## 2. 처음 접근
- 각 명령어에 대한 set 내장함수 이용

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    command = input().rstrip()

    if command == "all":
        S = set(range(1, 21))
    elif command == "empty":
        S.clear()
    else:
        command, x = command.split()
        x = int(x)
        if command == "add":
            S.add(x)
        elif command == "remove":
            S.discard(x)
        elif command == "check":
            print("1" if x in S else "0")
        elif command == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)

```

## 4. 개선 포인트
- 비트 마스킹 풀이로 훨씬 효율적인 풀이 가능
- set 대신 정수 하나만 씀 -> 메모리 사용 감소
- 비트 연산을 통해 매우 빠른 연산 가능

## 5. 재작성 코드
```python
 import sys

input = sys.stdin.readline

M = int(input())
S = 0

for _ in range(M):
    command = input().split()

    if command[0] == "add":
        x = int(command[1])
        S |= 1 << x
    elif command[0] == "remove":
        x = int(command[1])
        S &= ~(1 << x)
    elif command[0] == "check":
        x = int(command[1])
        sys.stdout.write("1\n" if S & (1 << x) else "0\n")
    elif command[0] == "toggle":
        x = int(command[1])
        S ^= 1 << x
    elif command[0] == "all":
        S = (1 << 21) - 2
    elif command[0] == "empty":
        S = 0
```

## 6. 배운점
- remove는 없는 값 시행시 오류 가능성 존재하므로 discard사용
- 위 같은 문제에서 out의 크기가 M만큼 커질 수 있으므로 check때마다 print

## 7. 풀이기록 
- 1차 풀이 : 2026-03-31
- 2차 풀이 : 2026-04-04
