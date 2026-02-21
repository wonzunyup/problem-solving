import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

ABC = str(A * B * C)
count = [0] * 10
for s in ABC:
    count[int(s)] += 1

for i in range(10):
    print(count[i])
