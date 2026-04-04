import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

cnt = 0
for coin in reversed(coins):
    cnt += K // coin
    K %= coin

print(cnt)
