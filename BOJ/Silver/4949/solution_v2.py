import sys

input = sys.stdin.readline

out = []
while True:
    string = input().rstrip()
    if string == ".":
        break

    stack = []
    for ch in string:
        if ch in "([":
            stack.append(ch)
        elif ch == "]":
            if not stack or stack.pop() != "[":
                out.append("no")
                break
        elif ch == ")":
            if not stack or stack.pop() != "(":
                out.append("no")
                break
    else:
        out.append("no" if stack else "yes")

sys.stdout.write("\n".join(out))
