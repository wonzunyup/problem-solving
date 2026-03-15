import sys
input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    string = input().rstrip()
    stack = []

    for ch in string:
        if ch == "(":
            stack.append(ch)
        else:
            if not stack:
                out.append("NO")
                break
            stack.pop()
    else:
        out.append("YES" if not stack else "NO")

sys.stdout.write("\n".join(out))
