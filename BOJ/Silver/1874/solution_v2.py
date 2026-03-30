import sys
input = sys.stdin.readline

n = int(input())

cur = 1
stack = []

out = []
for _ in range(n) :
    target = int(input())
    
    while cur <= target :
        stack.append(cur)
        out.append("+")
        cur += 1
    
    if stack and stack[-1] == target :
        stack.pop()
        out.append("-")
    else :
        print("NO")
        break
else :
    sys.stdout.write("\n".join(out))
