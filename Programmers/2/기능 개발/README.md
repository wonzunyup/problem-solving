# Programmers - 기능 개발

## 1. 문제 유형
- 큐

## 2. 처음 접근
- 리스트 활용

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline


def solution(progresses, speeds):
    answer = []
    while progresses:
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses :
            if progresses[0] >= 100 :
                count += 1
                progresses.pop(0)
                speeds.pop(0)
            else :
                break
        if count != 0 :
            answer.append(count)

    return answer

```

## 4. 개선 포인트
- 루프, 조건문 간소화

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline


def solution(progresses, speeds):
    answer = []
    while progresses:
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses and progresses[0] >= 100 :
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        if count != 0 :
            answer.append(count)

    return answer

```

## 6. 배운점
- X

## 7. 풀이기록 
- 1차 풀이 : 2026-05-22
