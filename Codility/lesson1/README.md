# Codility - lesson1

## 1. 문제 유형
- 비트 조작 / 진법 변환 (십진수 → 이진수)
- 문자열 선형 순회, 연속 구간 길이 세기
- 시간복잡도 목표: O(log N) — 이진 표현 길이에 비례

## 2. 처음 접근
- 이진수 직접 계산 후, 인덱스 위치별로 gap 위치 계산 

## 3. 제출 코드
```python
def solution(N):
    max_gap = 0
    binary = ""
    
    while N > 1 :
        binary += str((N % 2))
        N //= 2
    binary += str(N)
    binary = binary[::-1]
    
    for i in range(len(binary)) :
        if binary[i] == '0' :
            temp = 0
            for j in range(i, len(binary)) :
                if binary[j] == '1' : break
                if j == len(binary) - 1 :
                    temp = 0
                    break
                temp += 1
            if temp > max_gap : max_gap = temp
    return max_gap
```

## 4. 개선 포인트
- 진법 변환 내장 함수
- 이중 루프 -> 단일 루프
- 특수 처리 제거  

## 5. 재작성 코드
```python
def solution(N):
    binary = bin(N)[2:]

    max_gap = 0 
    current = 0
    counting = False 

    for ch in binary : 
        if ch == '1' :
            if counting and current > max_gap :
                max_gap = current
            current = 0
            counting = True
        else :
            if counting :
                current += 1

    return max_gap
```

## 6. 배운점
- 예외 조건 생각

## 7. 풀이기록 
- 1차 풀이 : 2026-11-25
