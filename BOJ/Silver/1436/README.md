# BOJ 1436 - 영화감독 숌

## 1. 문제 유형
- 브루트포스 / 문자열 패턴

## 2. 처음 접근
- num을 하나씩 올려 완전탐색

## 3. 제출 코드
```python
N = int(input())

num = 666
count = 0

while True:
    if "666" in str(num):
        count += 1
    if count == N:
        break
    num += 1

print(num)
```

## 4. 개선 포인트
- 종료 조건 위치 수정

## 5. 재작성 코드
```python
N = int(input())

num = 666
count = 0

while True:
    if "666" in str(num):
        count += 1
        if count == N:
            print(num)
            break
    num += 1
```

## 6. 배운점
- N의 범위에 따른 접근 방식 판단 

## 7. 풀이기록 
- 1차 풀이 : 2026-03-01
- 2차 풀이 : 2026-03-27
