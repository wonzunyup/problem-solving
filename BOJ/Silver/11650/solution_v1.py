import sys
input = sys.stdin.readline

N = int(input())

spots = [list(map(int, input().split())) for _ in range(N)]
spots.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    sys.stdout.write(str(spots[i][0]) + " " + str(spots[i][1]) + "\n")
