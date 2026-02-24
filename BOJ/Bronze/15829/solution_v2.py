import sys

input = sys.stdin.readline

MOD = 1234567891
r = 31

L = int(input())
string = input().strip()

hash_val = 0
power = 1

for ch in string:
    hash_val += (power * (ord(ch) - 96)) % MOD
    power = (power * r) % MOD

print(hash_val)
