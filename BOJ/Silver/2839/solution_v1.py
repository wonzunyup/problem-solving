N = int(input())

least = -1
five = 0

while 5 * five <= N:
    count = five
    temp = N
    temp -= 5 * five
    if temp % 3 == 0:
        count += temp // 3
        least = count
    five += 1

print(least)
