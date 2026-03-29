from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
josephus = deque(i for i in range(1, N + 1))

out = []
while josephus:
    josephus.rotate(-(K - 1))
    out.append(josephus.popleft())

sys.stdout.write("<" + ", ".join(map(str, out)) + ">")
