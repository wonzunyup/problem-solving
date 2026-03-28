import sys

input = sys.stdin.readline

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
rank = [1] * N

for i in range(N):
    for j in range(N):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank[i] += 1

sys.stdout.write(" ".join(map(str, rank)))
