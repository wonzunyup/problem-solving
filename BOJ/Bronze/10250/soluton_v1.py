import sys
input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    H, W, N = map(int, input().split())
    num = (N + H - 1) // H
    floor = N % H
    if floor == 0:
        floor = H
    out.append(str(floor) + "0" + str(num) + "\n")

sys.stdout.write("".join(out))
