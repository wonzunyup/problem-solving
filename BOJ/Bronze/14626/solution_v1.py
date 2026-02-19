import sys
input = sys.stdin.readline

ISBN = input()
m = int(ISBN[12])

total = 0
for i in range(12):
    if ISBN[i] == "*":
        continue
    if i % 2 == 0:
        total += int(ISBN[i])
    else:
        total += 3 * int(ISBN[i])

pos = ISBN.find("*")
num = 0
while True:
    if pos % 2 == 0 and m == 10 - (total + num) % 10:
        break
    elif pos % 2 == 1 and m == 10 - (total + 3 * num) % 10:
        break
    else:
        num += 1
print(num)
