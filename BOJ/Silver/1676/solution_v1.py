N = int(input())

def fact(x):
    r = 1
    for i in range(1, x + 1):
        r *= i
    return r

num = str(fact(N))

count = 0
for i in range(len(num) - 1, -1, -1):
    if num[i] != "0":
        print(count)
        break
    else:
        count += 1
