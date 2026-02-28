# BOJ 1181 - 단어 정렬

## 1. 문제 유형
- 정렬 / 문자열 / 중복제거

## 2. 처음 접근
- 파이썬 내장 정렬, 람다식을 통해 정렬

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

N = int(input())

words = []
for _ in range(N):
    words.append(input().strip())

words = set(words)
words = list(words)
words.sort(key=lambda x: (len(x), x))

sys.stdout.write("\n".join(words))
```

## 4. 개선 포인트
- 입출력 가독성, 효율 개선

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

N = int(input())

words = {input().strip() for _ in range(N)}
words = list(words)
words.sort(key=lambda x: (len(x), x))

sys.stdout.write("\n".join(words))
```

## 6. 배운점
- 파이썬은 웬만한 정렬은 내장 정렬을 사용해 정렬, 람다식을 통한 다중 기준 정렬, set을 통한 중복제거

## 7. 풀이기록 
- 1차 풀이 : 2026-02-28
