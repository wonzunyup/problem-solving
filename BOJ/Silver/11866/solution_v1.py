from collections import deque

N, K = map(int, input().split())

nums = deque(i for i in range(1, N + 1))
josephus = []

for _ in range(N):
    nums.rotate(-(K - 1))
    josephus.append(nums.popleft())

print("<" + ", ".join(map(str, josephus)) + ">")
