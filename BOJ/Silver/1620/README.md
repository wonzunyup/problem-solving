# BOJ 1620 - 나는야 포켓몬 마스터 이다솜

## 1. 문제 유형
- 해시 / 딕셔너리

## 2. 처음 접근
- 딕셔너리 두개를 통해 이름을 통한 접근, 번호를 통한 접근

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_dict = {}
name_dict = {}

out = []
for i in range(N):
    name = input().rstrip()
    num_dict[i + 1] = name
    name_dict[name] = i + 1

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        out.append(num_dict[int(question)])
    else:
        out.append(str(name_dict[question]))

sys.stdout.write("\n".join(out))

```

## 4. 개선 포인트
- X

## 5. 풀이기록 
- 1차 풀이 : 2026-03-31
