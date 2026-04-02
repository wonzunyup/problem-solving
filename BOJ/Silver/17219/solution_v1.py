import sys

input = sys.stdin.readline

N, M = map(int, input().split())

passwords = dict()
for _ in range(N):
    address, password = input().split()
    passwords[address] = password

out = []
for _ in range(M):
    out.append(passwords[input().rstrip()])

sys.stdout.write("\n".join(out))
