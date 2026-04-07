# BOJ 9375 - 패션왕 신해빈

## 1. 문제 유형
- 딕셔너리 / 경우의 수 / 조합

## 2. 처음 접근
-입는경우 / 안입는 경우로 나눠서 조합

## 3. 제출 코드
```python
from collections import defaultdict
import sys

input = sys.stdin.readline

T = int(input())

out = []
for _ in range(T):
    n = int(input())
    clothes = defaultdict(list)

    for _ in range(n):
        name, kind = input().split()
        clothes[kind].append(name)

    result = 1
    for clothe in clothes.values():
        result *= len(clothe) + 1
    out.append(str(result - 1))

sys.stdout.write("\n".join(out))

```

## 4. 개선 포인트
- 옷 이름은 사실 필요 없어서 옷 개수만 관리

## 5. 재작성 코드
```python
from collections import defaultdict
import sys

input = sys.stdin.readline

T = int(input())

out = []
for _ in range(T):
    n = int(input())
    clothes = defaultdict(int)

    for _ in range(n):
        name, kind = input().split()
        clothes[kind] += 1

    result = 1
    for cnt in clothes.values():
        result *= cnt + 1
    out.append(str(result - 1))

sys.stdout.write("\n".join(out))
```

## 6. 배운점
- 키가 없을 때 기본값이 필요한 경우(0, [], set()) defaultdict 활용

## 7. 풀이기록 
- 1차 풀이 : 2026-04-07
