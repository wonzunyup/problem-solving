# BOJ 30802 - 웰컴 키트

## 1. 문제 유형
- 수학

## 2. 처음 접근
- 티셔츠 묶음 수는 올림 나눗셈, 펜은 P로 나눈 몫, 나머지 

## 3. 제출 코드
```python
N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

num = 0
for size in sizes : 
  if size % T == 0 :
    num += size // T
  else : num += size // T + 1
print(num)
print(N // P, N % P)
```

## 4. 개선 포인트
- 올릿 나눗셈 코드 간단하게 수정, 변수 이름 명료화

## 5. 재작성 코드
```python
N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

shirt_packages = sum((s + T - 1) // T for s in sizes)
print(shirt_packages)
print(N // P, N % P)
```

## 6. 배운점
- 기초 연산 간단화 하기, 제네레이터 활용, 변수 이름 명료화
