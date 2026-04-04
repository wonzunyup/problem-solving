import sys

input = sys.stdin.readline

M = int(input())

S = 0
for _ in range(M):
    command = input().split()

    if command[0] == "add":
        x = int(command[1])
        S |= 1 << x
    elif command[0] == "remove":
        x = int(command[1])
        S &= ~(1 << x)
    elif command[0] == "check":
        x = int(command[1])
        sys.stdout.write("1\n" if S & (1 << x) else "0\n")
    elif command[0] == "toggle":
        x = int(command[1])
        S ^= 1 << x
    elif command[0] == "all":
        S = (1 << 21) - 2
    elif command[0] == "empty":
        S = 0
