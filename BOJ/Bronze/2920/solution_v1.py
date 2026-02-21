import sys

input = sys.stdin.readline

melody = list(map(int, input().split()))

type = ""
if melody[0] <= melody[1]:
    type = "ascending"
    for i in range(1, 8):
        if melody[i - 1] <= melody[i]:
            continue
        else:
            type = "mixed"
            break
elif melody[0] >= melody[1]:
    type = "descending"
    for i in range(1, 8):
        if melody[i - 1] >= melody[i]:
            continue
        else:
            type = "mixed"
            break
print(type)
