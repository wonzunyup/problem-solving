import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
nums = deque([i for i in range(1, N + 1)])

while len(nums) > 1:
    nums.popleft()
    nums.append(nums[0])
    nums.popleft()

print(nums[0])
