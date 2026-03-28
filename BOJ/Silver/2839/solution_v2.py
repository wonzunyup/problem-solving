import sys

input = sys.stdin.readline

N = int(input())

for i in range(N // 5, -1, -1):
    remain = N - 5 * i
    if remain % 3 == 0:
        print(i + remain // 3)
        break
else:
    print(-1)
