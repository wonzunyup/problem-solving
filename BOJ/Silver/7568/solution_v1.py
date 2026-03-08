import sys
input = sys.stdin.readline

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    rank = 1
    for j in range(N):
        if j != i:
            if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
                rank += 1
    print(rank, end = " ")
