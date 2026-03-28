# BOJ 1920 - 수 찾기

## 1. 문제 유형
- 자료구조(set) / 이분 탐색

## 2. 처음 접근
- in 연산자를 이용하여 탐색

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

N = int(input())
nnums = set(map(int, input().split()))

M = int(input())
mnums = list(map(int, input().split()))

for num in mnums:
    sys.stdout.write("1" + "\n") if num in nnums else sys.stdout.write("0" + "\n")
```

## 4. 개선 포인트
- 코드 간소화
- 이분 탐색 버전 풀이

## 5. 재작성 코드
```python
import sys

input = sys.stdin.readline

N = int(input())
nums = set(map(int, input().split()))

M = int(input())
for num in map(int, input().split()):
    sys.stdout.write("1\n" if num in nums else "0\n")
```
```python
import sys
input = sys.stdin.readline

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == arr[mid]:
            return 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return 0

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

M = int(input())
for num in map(int, input().split()):
    print(binary_search(nums, num))
```

## 6. 배운점
- set은 내부적으로 해시 테이블로 구현되어있어 탐색 시간이 O(1)이므로 탐색 시 리스트 말고 set 사용

## 7. 풀이기록 
- 1차 풀이 : 2026-03-09
- 2차 풀이 : 2026-03-28
