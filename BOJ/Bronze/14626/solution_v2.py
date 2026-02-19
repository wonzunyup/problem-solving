import sys
input = sys.stdin.readline

ISBN = input().strip()
m = int(ISBN[12])

total = 0
pos = ISBN.find("*")

for i in range(12):
    if ISBN[i] == "*":
        continue
    w = 1 if i % 2 == 0 else 3
    total += w * int(ISBN[i])

w_missing = 1 if pos % 2 == 0 else 3
for num in range(10):
    temp = total + w_missing * num
    if m == (10 - (temp % 10)) % 10:
        print(num)
        break
