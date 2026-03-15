import sys
input = sys.stdin.readline

T = int(input())
out = []
for _ in range(T):
    string = input().rstrip()
    if string == ".":
        break
    stack = []

    for ch in string:
        if ch in "([":
            stack.append(ch)
        elif ch == "]":
            if not stack or stack.pop() != "[":
                out.append("NO")
                break
        elif ch == ")":
            if not stack or stack.pop() != "(":
                out.append("NO")
                break
        else:
            continue
    else:
        if stack:
            out.append("NO")
        else:
            out.append("YES")

sys.stdout.write("\n".join(out))
