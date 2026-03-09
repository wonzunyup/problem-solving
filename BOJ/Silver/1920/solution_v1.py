import sys
input = sys.stdin.readline

N = int(input())
nnums = set(map(int, input().split()))

M = int(input())
mnums = list(map(int, input().split()))

for num in mnums:
    sys.stdout.write("1" + "\n") if num in nnums else sys.stdout.write("0" + "\n")
