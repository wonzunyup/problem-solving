# BOJ 17219 - 비밀번호 찾기

## 1. 문제 유형
- 딕셔너리

## 2. 처음 접근
- 딕셔너리에 저장 후 , 사이트 주소를 통한 탐색

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

passwords = dict()
for _ in range(N):
    address, password = input().split()
    passwords[address] = password

out = []
for _ in range(M):
    out.append(passwords[input().rstrip()])

sys.stdout.write("\n".join(out))
```

## 4. 개선 포인트
- X


## 5. 배운점
- X

## 6. 풀이기록 
- 1차 풀이 : 2026-04-02 
