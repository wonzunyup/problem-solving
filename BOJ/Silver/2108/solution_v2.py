from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

total = sum(nums)
if total >= 0:
    mean = int(total / N + 0.5)
else:
    mean = int(total / N - 0.5)
print(mean)

print(nums[N // 2])

counter = Counter(nums)
max_freq = max(counter.values())
modes = [num for num, freq in counter.items() if freq == max_freq]
modes.sort()
print(modes[1] if len(modes) > 1 else modes[0])

print(nums[-1] - nums[0])
