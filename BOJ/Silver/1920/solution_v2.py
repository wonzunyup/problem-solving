import sys

input = sys.stdin.readline


def bi_search(arr, n):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if n < arr[mid]:
            right = mid - 1
        elif n > arr[mid]:
            left = mid + 1
        else:
            return 1

    return 0


input()
nums = list(map(int, input().split()))
nums.sort()

input()
for num in list(map(int, input().split())):
    print(bi_search(nums, num))
