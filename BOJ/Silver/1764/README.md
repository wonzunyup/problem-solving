# BOJ 1764 - 듣보잡

## 1. 문제 유형
- 집합

## 2. 처음 접근
- in을 통해 교집합 확인

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ns = set(input().rstrip() for _ in range(N))
ms = set(input().rstrip() for _ in range(M))

out = []
for person in ns:
    if person in ms:
        out.append(person)

out.sort()
sys.stdout.write(str(len(out)) + "\n")
sys.stdout.write("\n".join(out))
```

## 4. 개선 포인트
- 교집합 연산을 통해 코드 간소화

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ns = set(input().rstrip() for _ in range(N))
ms = set(input().rstrip() for _ in range(M))

out = sorted(ns & ms)
sys.stdout.write(str(len(out)) + "\n")
sys.stdout.write("\n".join(out))
```

## 6. 배운점
- sorted를 통해 새로운 리스트 생성

## 7. 풀이기록 
- 1차 풀이 : 2026-04-01
- 2차 풀이 : 2026-04-04
