import sys

input = sys.stdin.readline

n = int(input())
seq = [int(input()) for _ in range(n)]

s = []
check = 0
cur = 1

out = []
for i in seq:
    if not s or s[-1] != i:
        s.append(cur)
        out.append("+")
        cur += 1
        while s[-1] != i:
            s.append(cur)
            out.append("+")
            cur += 1
            if cur > n + 1:
                check = 1
                break
    if check == 1:
        print("NO")
        break
    if s[-1] == i:
        s.pop()
        out.append("-")
else:
    sys.stdout.write("\n".join(out))
