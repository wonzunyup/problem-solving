import sys

input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    command = input().rstrip()

    if "all" in command:
        S = set([i for i in range(1, 21)])
    elif "empty" in command:
        S.clear()
    else:
        command, x = command.split()
        x = int(x)
        if command == "add":
            S.add(x)
        elif command == "remove":
            S.discard(x)
        elif command == "check":
            print("1" if x in S else "0")
        elif command == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
