import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque()
out = []

for _ in range(N):
    command = input().split()

    if command[0] == "push":
        q.append(command[1])
    elif command[0] == "pop":
        out.append(q.popleft() if q else "-1")
    elif command[0] == "size":
        out.append(str(len(q)))
    elif command[0] == "empty":
        out.append("1" if not q else "0")
    elif command[0] == "front":
        out.append(q[0] if q else "-1")
    elif command[0] == "back":
        out.append(q[-1] if q else "-1")

sys.stdout.write("\n".join(out))
