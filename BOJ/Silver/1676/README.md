# BOJ 1676 - 팩토리얼 0의 개수

## 1. 문제 유형
- 수학 / 소인수분해 개념 적용

## 2. 처음 접근
- 팩토리얼의 값을 구한 뒤 0이 아닌 숫자가 나올 때 까지 탐색

## 3. 제출 코드
```python
N = int(input())

def fact(x):
    r = 1
    for i in range(1, x + 1):
        r *= i
    return r

num = str(fact(N))

count = 0
for i in range(len(num) - 1, -1, -1):
    if num[i] != "0":
        print(count)
        break
    else:
        count += 1
```

## 4. 개선 포인트
- 수학적 개념 적용하여 효율성 증대
- 팩토리얼에서 뒤에 0이 나오는 이유는 인수로 2와 5를 가지고 있기 때문
- 따라서 N! 속 5의 개수를 구하여 풀이
- 위 접근을 통해 메모리, 시간 복잡도 효율 증가
- 기존 방식 : 큰 정수 저장, O(N x 큰수곱셈) -> 개선 방식 : 거의 X, O(logN)

## 5. 재작성 코드
```python
N = int(input())

count = 0
while N >= 5:
    N //= 5
    count += N

print(count)
```

## 6. 배운점
- 단순히 알고리즘 적으로 접근하지 말고 수학적인 접근 필요

## 7. 풀이기록 
- 1차 풀이 : 2026-03-01
- 2차 풀이 : 2026-03-27
