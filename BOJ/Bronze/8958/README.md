# BOJ 8985 - OX퀴즈

## 1. 문제 유형
- 구현 / 누적합

## 2. 처음 접근
- 임시 변수를 활용하여 O의 연속성 반영
- X일 시 초기화

## 3. 제출 코드
```python
N = int(input())

for _ in range(N):
    result = input().strip()
    score = 0
    temp = 0
    for s in result:
        if s == "O":
            temp += 1
            score += temp
        else:
            temp = 0
    print(score)
```

## 4. 개선 포인트
- 출력 모아서 한 번에 해도 좋음, but 길이가 짧아서 print만으로 충분

## 5. 재작성 코드
- X

## 6. 배운점
- X

## 7. 풀이기록 
- 1차 풀이 : 2026-02-22
