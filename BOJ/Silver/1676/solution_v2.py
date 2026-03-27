import sys

input = sys.stdin.readline

N = int(input())

nums = [i for i in range(1, N + 1)]
five = 0
for i in nums:
    while i % 5 == 0:
        five += 1
        i //= 5
print(five)
