from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]
nums.sort()

total = sum(nums)
if total >= 0:
    mean = int((total / N) + 0.5)
else:
    mean = int((total / N) - 0.5)
print(mean)

median = nums[N // 2]
print(median)

commons = Counter(nums).most_common()
modes = []
for i in range(len(commons)):
    if commons[i][1] == commons[0][1]:
        modes.append(commons[i][0])
modes.sort()
if len(modes) >= 2:
    mode = modes[1]
else:
    mode = modes[0]
print(mode)

ran = nums[-1] - nums[0]
print(ran)
