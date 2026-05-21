# Programmers - 같은 숫자는 싫어

## 1. 문제 유형
- 배열 / 구현 / 스택 

## 2. 처음 접근
- answer가 비어있지 않고 넣으려는 숫자와 가장 최근의 숫자가 같을시 continue

## 3. 제출 코드
```python
def solution(arr):
    answer = []
    for i in arr : 
        if answer and i == answer[-1] :
            continue
        else :
            answer.append(i) 
    return answer
```

## 4. 개선 포인트
- X

## 5. 풀이기록 
- 1차 풀이 : 2026-05-20
