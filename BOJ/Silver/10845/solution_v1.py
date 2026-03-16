import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
q = deque()

out = []
for _ in range(N):
    command = input().split()
    if command[0] == "push":
        value = command[1]
        q.append(value)
    elif command[0] == "pop":
        out.append(q.popleft() if q else "-1")
    elif command[0] == "size":
        out.append(str(len(q)))
    elif command[0] == "empty":
        out.append("1" if not q else "0")
    elif command[0] == "front":
        out.append(q[0] if q else "-1")
    elif command[0] == "back":
        out.append(str(q[len(q) - 1]) if q else "-1")

sys.stdout.write("\n".join(out))
