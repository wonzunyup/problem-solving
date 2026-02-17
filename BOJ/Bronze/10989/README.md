# BOJ 10989 - 수 정렬하기 3

## 1. 문제 유형
- 정렬

## 2. 처음 접근
- 파이썬 내장 정렬 활용

## 3. 제출 코드
```python
N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()
for i in range(N) :
  print(nums[i])
```

## 4. 개선 포인트
- 메모리 초과
- nums = [int(input()) for _ in range(N)] 로 인해 N개의 정수를 리스트에 모두 저장하게됨
- 파이썬 int는 객체이고, 리스트 또한 포인터 배열이기 때문에 추가 오버헤드 증가
- 입력 값 범위가 1~10000 고정이기 때문에 리스트에 전부 저장하는 것이 아닌 개수만 카운트
- 값 범위가 작고 입력 개수가 큰 경우 -> 계수 정렬 활용

## 5. 재작성 코드
```python
import sys
input = sys.stdin.readline

N = int(input())
cnt = [0] * 10001

for _ in range(N) :
  cnt[int(input())] += 1

out = []
for x in range(1, 10001) :
  if cnt[x] :
    sys.stdout.write((str(x) + "\n") * cnt[x])
```

## 6. 배운점
- 입력 값 범위, 개수에 따른 효과적인 알고리즘 채택 필요
- 효율적인 입/출력 방식을 통해 시간/공간 복잡도 개선

## 7. 풀이기록 
- 1차 풀이 : 2026-02-16
