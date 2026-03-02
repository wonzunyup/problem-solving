# BOJ 2751 - 수 정렬하기 2

## 1. 문제 유형
- 

## 2. 처음 접근
- set을 통한 중복 제거, 퀵정렬을 통한 정

## 3. 제출 코드
```python
import sys


def quick_sort(arr, left, right):
    if left >= right:
        return

    pivot = arr[(left + right) // 2]
    i = left
    j = right

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    quick_sort(arr, left, j)
    quick_sort(arr, i, right)


input = sys.stdin.readline

N = int(input())

nums = set()
for i in range(N):
    nums.add(int(input()))

nums = list(nums)
quick_sort(nums, 0, N - 1)

for i in nums:
    sys.stdout.write(str(i) + "\n")
```

## 4. 개선 포인트
- 내장정렬 사용하여 코드 간소화, 효율성 증대

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums = set(nums)
nums = list(nums)
nums.sort()

sys.stdout.write("\n".join(map(str, nums)))
```

## 6. 배운점
- 파이썬의 경우 대부분의 경우에서 내장정렬을 사용하는 것이 효과적
- N이 크고 범위가 N의 개수와 비슷하거나 작을 시 카운팅 정렬이 효과적

## 7. 풀이기록 
- 1차 풀이 : 2026-03-02
