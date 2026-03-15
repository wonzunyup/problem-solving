import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())
nums = list(map(int, input().split()))
c = Counter(nums)

out = []
M = int(input())
for num in map(int, input().split()):
    out.append(str(c[num]))

sys.stdout.write(" ".join(out))
