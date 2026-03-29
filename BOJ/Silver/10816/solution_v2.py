from collections import Counter
import sys

input = sys.stdin.readline

input()
counter = Counter(map(int, input().split()))

cnt = []
input()
for num in map(int, input().split()):
    cnt.append(counter[num])

sys.stdout.write(" ".join(map(str, cnt)))
