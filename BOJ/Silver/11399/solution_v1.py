import sys

input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
times.sort()

total = 0
acc = 0
for time in times:
    total += acc + time
    acc += time
    
sys.stdout.write(str(total))
