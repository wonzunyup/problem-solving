import sys

input = sys.stdin.readline

input()
nums = set(map(int, input().split()))

input()
for num in list(map(int, input().split())):
    print(1 if num in nums else 0)
