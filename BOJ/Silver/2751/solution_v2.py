import sys

input = sys.stdin.readline

N = int(input())
nums = set(int(input()) for _ in range(N))
nums = list(nums)
nums.sort()

sys.stdout.write("\n".join(map(str, nums)))
