import sys
input = sys.stdin.readline

out = []
while True:
    string = input().rstrip()
    if string == ".":
        break
    stack = []

    for ch in string:
        if ch == "[" or ch == "(":
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
            continue
    else:
        if stack:
            out.append("no")
        else:
            out.append("yes")

sys.stdout.write("\n".join(out))
