from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

q = deque()
out = []
for _ in range(N):
    command = input().rstrip()
    if "push" in command:
        command, value = command.split()
        q.append(value)
    elif command == "pop":
        out.append(q.popleft() if q else "-1")
    elif command == "size":
        out.append(str(len(q)))
    elif command == "empty":
        out.append("0" if q else "1")
    elif command == "front":
        out.append(q[0] if q else "-1")
    elif command == "back":
        out.append(q[-1] if q else "-1")

sys.stdout.write("\n".join(out))
