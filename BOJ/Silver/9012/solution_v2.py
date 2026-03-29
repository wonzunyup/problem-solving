import sys

input = sys.stdin.readline

T = int(input())

out = []
for _ in range(T):
    vps = input().rstrip()

    stack = []
    for ch in vps:
        if ch == "(":
            stack.append(ch)
        else:
            if not stack or stack.pop() != "(":
                out.append("NO")
                break
    else:
        out.append("NO" if stack else "YES")

sys.stdout.write("\n".join(out))
