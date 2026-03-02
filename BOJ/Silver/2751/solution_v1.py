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
